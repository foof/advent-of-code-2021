

def solve(outputs):
    return len([digit for sublist in [output.split(' ') for output in outputs] for digit in sublist if len(digit) in [2, 4, 3, 7]])


if __name__ == "__main__":
    with open('./input', 'r') as f:
        outputs = [line.split(" | ")[1] for line in f.read().splitlines()]
        print(solve(outputs))
