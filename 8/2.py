
digit_map = {"abcefg": "0", "cf": "1", "acdeg": "2", "acdfg": "3", "bcdf": "4", "abdfg": "5", "abdefg": "6", "acf": "7", "abcdefg": "8", "abcdfg": "9"}


def solve_line(line):
    mapping = {}
    line = line.split(' | ')
    input_data, output_data = line[0].split(' '), line[1].split(' ')
    input_data.sort(key=lambda x: len(x))

    temp_input_data = ["".join(sorted(list(digit))) for digit in input_data]

    # Determine "a"
    mapping[[char for char in input_data[1] if char not in input_data[0]][0]] = 'a'
    temp_input_data = reduce_digits(temp_input_data, mapping)

    # Determine "e"
    two_index = 0
    e_chars = list("".join([digit for digit in temp_input_data[2:6]]))
    e_char = [char for char in e_chars if e_chars.count(char) == 1][0]
    for idx, digit in enumerate(digit for digit in temp_input_data[2:6]):
        if e_char in list(digit):
            two_index = 2+idx
    mapping[e_char] = 'e'
    temp_input_data = reduce_digits(temp_input_data, mapping)

    # Determine "c"
    for digit in temp_input_data[2:6]:
        pass
    mapping[[char for char in list(temp_input_data[two_index]) if char in list(temp_input_data[0])][0]] = 'c'
    temp_input_data = reduce_digits(temp_input_data, mapping)

    # Determine "f"
    mapping[temp_input_data[0]] = 'f'
    temp_input_data = reduce_digits(temp_input_data, mapping)

    # Determine "d"
    mapping[[char for char in list(temp_input_data[two_index]) if char in list(temp_input_data[2])][0]] = 'd'
    temp_input_data = reduce_digits(temp_input_data, mapping)

    # Determine "b"
    mapping[temp_input_data[2]] = 'b'
    temp_input_data = reduce_digits(temp_input_data, mapping)

    # Determine "g"
    mapping[temp_input_data[-1]] = 'g'
    temp_input_data = reduce_digits(temp_input_data, mapping)

    return int("".join([digit_map[digit] for digit in [translate(digit, mapping) for digit in output_data]]))


def translate(digit, mapping):
    real_digit = ""
    for char in list(digit):
        real_digit += mapping[char]
    real_digit = "".join(sorted(list(real_digit)))
    return real_digit


def reduce_digits(digits, mapping):
    for seg_1 in mapping:
        digits = [digit.replace(seg_1, '') for digit in digits]
    return digits


def solve(lines):
    return sum(solve_line(line) for line in lines)


if __name__ == "__main__":
    with open('./input', 'r') as f:
        print(solve(f.read().splitlines()))
