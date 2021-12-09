
def solve(grid):
    new_grid = {}
    neighbour_deltas = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    for point, cell in grid.items():
        lower_neighbours = [1 for delta in neighbour_deltas if (point[0]+delta[0], point[1]+delta[1]) in grid and grid[(point[0]+delta[0], point[1]+delta[1])] <= cell]
        if not len(lower_neighbours):
            new_grid[point] = cell
    return sum([cell+1 for cell in new_grid.values()])


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        grid = {(x, y): int(cell) for y, row in enumerate(lines) for x, cell in enumerate(list(row))}
        print(solve(grid))
