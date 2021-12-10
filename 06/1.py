
from typing import List


def solve(state: List[int]):
    for _ in range(80):
        new_spawn_count = state.count(0)
        state = [fish-1 if fish > 0 else 6 for fish in state]
        for _ in range(new_spawn_count):
            state.append(8)
    return len(state)


if __name__ == "__main__":
    with open('./input', 'r') as f:
        initial_state = list(map(int, f.read().split(',')))
        print(solve(initial_state))
