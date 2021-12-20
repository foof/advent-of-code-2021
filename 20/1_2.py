
def solve(binary_map, image, steps):
    n_tuples = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    for step in range(steps):
        all_on = step % 2 != 0
        min_x = min(x for x, y in image)
        max_x = max(x for x, y in image)
        min_y = min(y for x, y in image)
        max_y = max(y for x, y in image)

        new_image = {}
        for x in range(min_x-2, max_x+2):
            for y in range(min_y-2, max_y+2):
                binary_num = ''
                for n_xy in n_tuples:
                    n = (x+n_xy[0], y+n_xy[1])

                    if n not in image:
                        if all_on:
                            pixel = '#'
                        else:
                            pixel = '.'
                    else:
                        pixel = image[n]

                    binary_num += pixel
                binary_num = binary_num.replace('.', '0').replace('#', '1')
                if x >= min_x - 1 and x <= max_x + 1 and y >= min_y - 1 and y <= max_y + 1:
                    new_image[(x, y)] = binary_map[int(binary_num, 2)]
        image = new_image

    return len([pixel for pixel in image.values() if pixel == '#'])


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        binary_map = list(lines[0])
        image = {(x, y): pixel for y, line in enumerate(lines[2:]) for x, pixel in enumerate(line)}
        print(solve(binary_map, image, 2))
        print(solve(binary_map, image, 50))
