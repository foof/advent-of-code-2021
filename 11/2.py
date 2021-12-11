

def solve(lines):
    octopi = {(x, y): octopus for y, row in enumerate(lines) for x, octopus in enumerate(row)}
    neighbour_deltas = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    step = 0
    while True:
        step += 1
        octopi = {point: octopus+1 for point, octopus in octopi.items()}

        flashed_octopi = []
        flashing_octopi = [point for point, octopus in octopi.items() if octopus > 9]
        saved_increments = {}

        while len(flashing_octopi):
            for point in flashing_octopi:
                flashed_octopi.append(point)
                for delta in neighbour_deltas:
                    n_point = (point[0]+delta[0], point[1]+delta[1])
                    if n_point in octopi:
                        if n_point in saved_increments:
                            saved_increments[n_point] += 1
                        else:
                            saved_increments[n_point] = 1
            flashing_octopi = []
            for point, value in saved_increments.items():
                octopi[point] += value

            flashing_octopi = [point for point, octopus in octopi.items() if octopus > 9 and point not in flashed_octopi]
            saved_increments = {}

        for point in flashed_octopi:
            octopi[point] = 0

        if len(flashed_octopi) == len(octopi):
            return step


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = [[int(num) for num in list(line)] for line in f.read().splitlines()]
        print(solve(lines))
