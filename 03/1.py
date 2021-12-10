
from typing import List


def solve(lines: List[str]):
    counts = {}
    for line in lines:
        for i, char in enumerate(list(line)):
            if i not in counts:
                counts[i] = int(char)
            else:
                counts[i] += int(char)

    gamma: List[str] = []
    epsilon: List[str] = []
    for i, count in counts.items():
        if count > len(lines)//2:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")

    return int("".join(gamma), 2) * int("".join(epsilon), 2)


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
