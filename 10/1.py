from typing import List

opening_brackets = ["<", "(", "[", "{"]
closing_brackets = {"<": ">", "(": ")", "[": "]", "{": "}"}
bracket_points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def solve_line(line: str):
    brackets = list(line)
    expected_closing_brackets = []
    for bracket in brackets:
        if bracket in opening_brackets:
            expected_closing_brackets.append(closing_brackets[bracket])
        elif not len(expected_closing_brackets) or bracket != expected_closing_brackets[-1]:
            return line, 'corrupt', bracket_points[bracket]
        else:
            expected_closing_brackets.pop()

    if len(expected_closing_brackets):
        return line, 'incomplete', None

    return line, 'valid', None


def solve(lines: List[str]):
    solved_lines = [solve_line(line) for line in lines]
    corrupt_scores = [line[2] for line in solved_lines if line[1] == 'corrupt']
    return sum([value * corrupt_scores.count(value) for value in bracket_points.values()])


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
