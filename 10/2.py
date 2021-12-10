from functools import reduce
from typing import List

opening_brackets = ["<", "(", "[", "{"]
closing_brackets = {"<": ">", "(": ")", "[": "]", "{": "}"}
bracket_points = {")": 1, "]": 2, "}": 3, ">": 4}


def solve_line(line: str):
    brackets = list(line)
    expected_closing_brackets = []
    for bracket in brackets:
        if bracket in opening_brackets:
            expected_closing_brackets.append(closing_brackets[bracket])
        elif not len(expected_closing_brackets):
            return 'corrupt', None
        elif bracket != expected_closing_brackets[-1]:
            return 'corrupt', None
        else:
            expected_closing_brackets.pop()

    if len(expected_closing_brackets):
        return 'incomplete', expected_closing_brackets

    return 'valid', None


def calc_score(brackets: List) -> int:
    return reduce(lambda acc, x: acc*5 + bracket_points[x], reversed(brackets), 0)


def solve(lines: List[str]) -> int:
    solved_lines = [solve_line(line) for line in lines]
    missing_brackets = [line[1] for line in solved_lines if line[0] == 'incomplete']
    scores = sorted([calc_score(brackets) for brackets in missing_brackets])
    return scores[len(scores)//2]


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
