
from typing import Dict, List, Tuple


def print_paper(paper):
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    for point in paper:
        min_x = min(min_x, point[0])
        min_y = min(min_y, point[1])
        max_x = max(max_x, point[0])
        max_y = max(max_y, point[1])

    for y in range(min_y, max_y+1):
        row = ""
        for x in range(min_x, max_x+1):
            if (x, y) in paper:
                row += "#"
            else:
                row += " "
        print(row)
    return


def fold(paper: Dict[Tuple[int, int], str], direction: str, index: int):
    new_paper = {}
    max_x, max_y = 0, 0
    for point in paper:
        max_x = max(max_x, point[0])
        max_y = max(max_y, point[1])

    if direction == "y":
        for y in range(0, index):
            for x in range(0, max_x+1):
                if (x, y) in paper:
                    new_paper[(x, y)] = "#"

        for y in range(index+1, max_y+1):
            for x in range(0, max_x+1):
                if (x, y) in paper:
                    new_y = index + (index - y)
                    new_paper[(x, new_y)] = '#'
    else:
        for y in range(0, max_y+1):
            for x in range(0, index):
                if (x, y) in paper:
                    new_paper[(x, y)] = paper[(x, y)]

        for y in range(0, max_y+1):
            for x in range(index+1, max_x+1):
                if (x, y) in paper:
                    new_x = index + (index - x)
                    new_paper[(new_x, y)] = '#'

    return new_paper


def solve(paper: Dict[Tuple[int, int], str], instructions: List[str]):
    for inst in instructions:
        direction, index = inst.split("=")
        paper = fold(paper, direction, int(index))

    return paper


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        paper = {}
        instructions = []
        for line in lines:
            if "," in line:
                x, y = line.split(',')
                paper[(int(x), int(y))] = '#'
            elif "=" in line:
                instructions.append(line.replace("fold along ", ''))

        print_paper(solve(paper, instructions))
