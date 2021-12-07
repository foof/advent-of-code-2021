
from typing import List

DP = {}


def calc_fuel_usage(start_pos, end_pos) -> int:
    steps = abs(end_pos - start_pos)
    if steps in DP:
        return DP[steps]
    fuel = 0
    for step in range(steps):
        fuel += 1 + step
    DP[steps] = fuel
    return fuel


def solve(crabs: List[int]):
    crabs.sort()
    best_usage = None
    for pos in range(crabs[0], crabs[-1]+1):
        fuel_usage = sum([calc_fuel_usage(crab, pos) for crab in crabs])
        if not best_usage or fuel_usage < best_usage:
            best_usage = fuel_usage

    return best_usage


if __name__ == "__main__":
    with open('./input', 'r') as f:
        print(solve(list(map(int, f.read().split(',')))))
