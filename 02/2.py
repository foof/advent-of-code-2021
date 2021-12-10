
def solve(lines):
    x, y, aim = 0, 0, 0
    for line in lines:
        cmd, val = line.split(' ')
        val = int(val)
        if cmd == 'forward':
            x = x+val
            y = y+aim*val
        elif cmd == 'up':
            aim = aim-val
        elif cmd == 'down':
            aim = aim+val

    return x*y


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
