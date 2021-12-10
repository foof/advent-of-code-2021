
from typing import List


def solve(crabs: List[int]):
    crabs.sort()
    best_usage = None
    for pos in range(crabs[0], crabs[-1]+1):
        fuel_usage = sum([abs(crab-pos) for crab in crabs])
        if not best_usage or fuel_usage < best_usage:
            best_usage = fuel_usage

    return best_usage


if __name__ == "__main__":
    with open('./input', 'r') as f:
        print(solve(list(map(int, f.read().split(',')))))
