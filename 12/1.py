
from typing import List

nodes = {}


def find_path(current_node: str, destination: str, visited: List, paths: List):
    if current_node != destination and current_node.islower() and current_node in visited:
        return

    visited = list(visited)
    visited.append(current_node)

    if current_node == destination:
        paths.append(visited)
        return

    for next_node in nodes[current_node]:
        find_path(next_node, destination, visited, paths)


def solve():
    paths = []
    find_path('start', 'end', [], paths)
    return len(paths)


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            parent, child = line.split('-')
            if parent not in nodes:
                nodes[parent] = []
            if child not in nodes:
                nodes[child] = []
            if child not in nodes[parent]:
                nodes[parent].append(child)
            if parent not in nodes[child]:
                nodes[child].append(parent)
        print(solve())
