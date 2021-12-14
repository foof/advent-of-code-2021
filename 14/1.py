
from collections import Counter
from typing import Dict


def solve(polymer: str, rules: Dict[str, str], steps: int):
    for _ in range(steps):
        new_polymer = list(polymer)
        for i in range(len(polymer)-1, -1, -1):
            if not i:
                continue
            new_polymer.insert(i, rules[polymer[i-1:i+1]])
        polymer = "".join(new_polymer)

    counter = Counter(polymer)
    return max(counter.values()) - min(counter.values())


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        polymer = ""
        rules = {}
        for line in lines:
            if "->" in line:
                pair, insertion = line.split(" -> ")
                rules[pair] = insertion
            elif line:
                polymer = line
        print(solve(polymer, rules, 10))
