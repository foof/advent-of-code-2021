
def solve(lines):
    x, y = 0, 0
    for line in lines:
        cmd, val = line.split(' ')
        val = int(val)
        if cmd == 'forward':
            x = x+val
        elif cmd == 'up':
            y = y-val
        elif cmd == 'down':
            y = y+val

    return x*y


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
