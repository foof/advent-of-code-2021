import heapq
import math


def reconstruct_path(came_from, current, nodes):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


def cost_of_path(path, nodes):
    return sum([nodes[node] for node in path[1:]])


def solve(start, end, nodes):
    max_x, max_y = 0, 0
    for node in nodes:
        max_x = max(max_x, node[0])
        max_y = max(max_y, node[1])

    def h(node):
        return abs(max_x-node[0]) + abs(max_y-node[0])

    open_set = [(float(0), int(start[0]), int(start[1]))]
    heapq.heapify(open_set)

    came_from = {}
    g_score = {node: math.inf for node in nodes.keys()}
    g_score[start] = 0
    f_score = {node: math.inf for node in nodes.keys()}
    f_score[start] = h(start)
    n_deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while len(open_set):
        current = heapq.heappop(open_set)
        current = (current[1], current[2])
        if current == end:
            return reconstruct_path(came_from, current, nodes)

        for delta in n_deltas:
            neighbour = (current[0]+delta[0], current[1]+delta[1])
            if neighbour not in nodes:
                continue

            tentative_g_score = g_score[current] + nodes[neighbour]
            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + h(neighbour)
                if neighbour not in open_set:
                    heapq.heappush(open_set, (f_score[neighbour], neighbour[0], neighbour[1]))

    return 'failed'


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        nodes = {(x, y): int(weight) for y, line in enumerate(lines) for x, weight in enumerate(line)}
        x_size = len(lines[0])
        y_size = len(lines)

        for y in range(0, y_size*5):
            for x in range(0, x_size*5):
                if y < y_size and x < x_size:
                    continue
                elif y >= y_size:
                    value = nodes[(x, y-y_size)] + 1
                else:
                    value = nodes[(x-x_size, y)] + 1
                if value > 9:
                    value = 1
                nodes[(x, y)] = value

        path = solve((0, 0), (x_size*5-1, y_size*5-1), nodes)
        cost = cost_of_path(path, nodes)
        print(cost)
