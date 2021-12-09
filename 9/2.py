import math


def find_basin_points(initial_point, grid):
    visited = []
    queue = [initial_point]
    while len(queue):
        point = queue.pop()

        if point not in visited:
            visited.append(point)

        neighbour_deltas = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        neighbours = [(point[0]+delta[0], point[1]+delta[1]) for delta in neighbour_deltas]
        neighbours = [n_point for n_point in neighbours if n_point in grid and grid[n_point] != 9]

        queue += [n for n in neighbours if n not in visited]

    return visited


def solve(grid):
    visited = []
    basins = []
    for point in grid:
        if grid[point] == 9 or point in visited:
            continue

        basin_points = find_basin_points(point, grid)
        visited += basin_points
        basins.append(len(basin_points))

    basins = sorted(basins)[-3:]

    return math.prod(basins)


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        grid = {(x, y): int(cell) for y, row in enumerate(lines) for x, cell in enumerate(list(row))}
        print(solve(grid))
