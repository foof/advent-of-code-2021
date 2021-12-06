
from collections import Counter
from typing import Dict


def solve(state: Dict[int, int]):
    for _ in range(256):
        new_state = Counter()
        for fish, count in state.items():
            new_state[fish-1 if fish > 0 else 6] += count
        new_state[8] = state[0]
        state = new_state
    return sum(state.values())


if __name__ == "__main__":
    with open('./input', 'r') as f:
        initial_state = list(map(int, f.read().split(',')))
        initial_dict = Counter(initial_state)
        print(solve(initial_dict))
