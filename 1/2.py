
def solve(lines):
    windows = [int(line) + int(lines[i+1]) + int(lines[i+2]) for i, line in enumerate(lines) if i+2 < len(lines)]

    increments = 0
    previousMeasurement = windows[0]
    for measurement in windows:
        if measurement > previousMeasurement:
            increments = increments+1
        previousMeasurement = measurement

    return increments


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
