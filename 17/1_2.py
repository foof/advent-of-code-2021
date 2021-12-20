
import re


def solve(x_bounds, y_bounds):
    hits = []
    velocities = []
    hit_max_y = 0
    for x in range(0, 130):
        for y in range(min(y_bounds), 150):
            velocities.append((x, y))

    for velocity in velocities:
        new_velocity = velocity
        pos = (0, 0)
        steps = []
        max_y = 0
        while pos[1] >= min(y_bounds):
            steps.append(pos)
            pos = (pos[0]+new_velocity[0], pos[1]+new_velocity[1])
            max_y = max(max_y, pos[1])

            if pos[0] >= x_bounds[0] and pos[0] <= x_bounds[1] and pos[1] >= y_bounds[0] and pos[1] <= y_bounds[1]:
                hits.append(velocity)
                hit_max_y = max(hit_max_y, max_y)
                break

            new_x_velocity = new_velocity[0]
            if new_x_velocity > 0:
                new_x_velocity -= 1
            elif new_x_velocity < 0:
                new_x_velocity += 1
            new_velocity = (new_x_velocity, new_velocity[1]-1)

    return hit_max_y, len(hits)


if __name__ == "__main__":
    with open('./input', 'r') as f:
        x1, x2, y1, y2 = map(int, re.findall('-?\d+', f.read().strip()))
        x_bounds, y_bounds = (x1, x2), (y1, y2)

        print(solve(x_bounds, y_bounds))
