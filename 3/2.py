
from typing import List


def find_most_common_bit(lines: List[str], pos) -> str:
    if sum([int(line[pos:pos+1]) for line in lines]) >= len(lines)/2:
        return "1"
    return "0"


def find_least_common_bit(lines: List[str], pos) -> str:
    if find_most_common_bit(lines, pos) == "1":
        return "0"
    return "1"


def oxygen_generator_rating(lines: List[str]) -> int:
    lines, pos = list(lines), 0
    while len(lines) > 1:
        most_common_bit = find_most_common_bit(lines, pos)
        lines = [line for line in lines if line[pos:pos+1] == most_common_bit]
        pos += 1
    return int(lines[0], 2)


def co2_scrubber_rating(lines: List[str]) -> int:
    lines, pos = list(lines), 0
    while len(lines) > 1:
        least_common_bit = find_least_common_bit(lines, pos)
        lines = [line for line in lines if line[pos:pos+1] == least_common_bit]
        pos += 1
    return int(lines[0], 2)


def solve(lines: List[str]) -> int:
    return oxygen_generator_rating(lines) * co2_scrubber_rating(lines)


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
