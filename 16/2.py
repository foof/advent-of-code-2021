
def handle_value(type, value, new_value):
    if value is None:
        value = new_value
    elif type == 0:
        value += new_value
    elif type == 1:
        value *= new_value
    elif type == 2:
        value = min(value, new_value)
    elif type == 3:
        value = max(value, new_value)
    elif type == 5:
        if value > new_value:
            value = 1
        else:
            value = 0
    elif type == 6:
        if value < new_value:
            value = 1
        else:
            value = 0
    elif type == 7:
        if value == new_value:
            value = 1
        else:
            value = 0

    return value


def parse_next_packet(bits):
    type = int(bits[3:6], 2)
    value = None

    if type == 4:
        literal = ""
        offset = 6
        while True:
            is_last = int(bits[offset:offset+1]) == 0
            literal += bits[offset+1:offset+5]
            offset += 5
            if is_last:
                value = int(literal, 2)
                break
        L = offset
    else:
        length_type = int(bits[6:7])
        if length_type:
            num_subpackets = int(bits[7:18], 2)
            L = 18
            sub_bits = bits[L:]
            for _ in range(num_subpackets):
                new_L, new_value = parse_next_packet(sub_bits)
                value = handle_value(type, value, new_value)
                L += new_L
                sub_bits = bits[L:]
        else:
            subpacket_length = int(bits[7:22], 2)
            L = 22 + subpacket_length
            sub_bits = bits[22:L]
            while len(sub_bits):
                new_L, new_value = parse_next_packet(sub_bits)
                value = handle_value(type, value, new_value)
                sub_bits = sub_bits[new_L:]

    return L, value


def solve(line):
    bin_length = len(line)*4
    spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=bin_length, type='b')
    hex = int(line, 16)
    remaining_bits = format(hex, spec)
    value = None

    while len(remaining_bits) > 7:
        L, value = parse_next_packet(remaining_bits)
        remaining_bits = remaining_bits[L:]

    return value


if __name__ == "__main__":
    with open('./input', 'r') as f:
        line = f.read().strip()
        print(solve(line))
