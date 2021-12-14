
from collections import Counter
from typing import Dict


def solve(polymer: str, rules: Dict[str, str], steps: int):
    # Initial pair counts
    pair_counts = Counter()
    for i in range(len(polymer)-1):
        pair_counts[polymer[i]+polymer[i+1]] += 1

    for _ in range(steps):
        new_pair_counts = Counter()
        for pair in pair_counts:
            # For example if there is a rule, AB -> C
            # Increment AC and CB with the number of occurrences of AB
            new_pair_counts[pair[0]+rules[pair]] += pair_counts[pair]
            new_pair_counts[rules[pair]+pair[1]] += pair_counts[pair]
        pair_counts = new_pair_counts

    char_counts = Counter()
    for pair in pair_counts:
        char_counts[pair[0]] += pair_counts[pair]
    char_counts[polymer[-1]] += 1

    return max(char_counts.values()) - min(char_counts.values())


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
        print(solve(polymer, rules, 40))
