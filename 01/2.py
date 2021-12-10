
def solve(lines):
    windows = [int(line) + int(lines[i+1]) + int(lines[i+2]) for i, line in enumerate(lines) if i+2 < len(lines)]
    return sum([1 for i, window in enumerate(windows) if i+1 < len(windows) and window < windows[i+1]])


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
