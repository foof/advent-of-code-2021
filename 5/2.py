from math import gcd


class CoordPair():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.dx = p2[0]-p1[0]
        self.dy = p2[1]-p1[1]
        divisor = gcd(abs(self.dx), abs(self.dy))
        self.dx = self.dx//divisor
        self.dy = self.dy//divisor

    def is_horizontal_or_vertical(self):
        return self.p1[0] == self.p2[0] or self.p1[1] == self.p2[1]


class Grid():
    def __init__(self, size_x, size_y):
        self.rows = [[0 for _ in range(size_x+1)] for _ in range(size_y+1)]

    def fill_line(self, pair: CoordPair):
        self.rows[pair.p1[1]][pair.p1[0]] += 1
        x, y = pair.p1[0], pair.p1[1]
        while x != pair.p2[0] or y != pair.p2[1]:
            x += pair.dx
            y += pair.dy
            self.rows[y][x] += 1

    def get_number_of_dangerous_areas(self):
        return sum([1 for row in self.rows for cell in row if cell > 1])


def solve(lines):
    max_x, max_y = 0, 0
    pairs = []
    for line in lines:
        p1, p2 = line.split(' -> ')
        p1 = tuple([int(num) for num in p1.split(',')])
        p2 = tuple([int(num) for num in p2.split(',')])
        pairs.append(CoordPair(p1, p2))
        max_x = max(p1[0], p2[0], max_x)
        max_y = max(p1[1], p2[1], max_y)

    grid = Grid(max_x, max_y)
    for pair in pairs:
        grid.fill_line(pair)

    return grid.get_number_of_dangerous_areas()


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
