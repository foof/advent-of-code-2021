
def solve(lines):
    lines = [int(x) for x in lines]
    increments = 0
    previousMeasurement = lines[0]
    for measurement in lines:
        if measurement > previousMeasurement:
            increments = increments+1
        previousMeasurement = measurement

    return increments


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
