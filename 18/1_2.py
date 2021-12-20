
import math
from collections import deque


class Node:
    left = None
    right = None
    parent = None

    def __init__(self, number=None):
        if number:
            self.set_left(number[0])
            self.set_right(number[1])

    def set_left(self, node):
        if type(node) == list:
            node = Node(node)

        self.left = node

        if type(node) == Node:
            node.parent = self

    def set_right(self, node):
        if type(node) == list:
            node = Node(node)

        self.right = node

        if type(node) == Node:
            node.parent = self

    def is_bottom(self):
        return type(self.left) == int and type(self.right) == int

    def find_depth(self):
        depth = 1
        n = self
        while n.parent:
            n = n.parent
            depth += 1
        return depth

    def reduce(self):
        node_to_explode = self.find_node_to_explode()
        node_to_split = self.find_node_to_split()
        while node_to_explode or node_to_split:
            if node_to_explode:
                node_to_explode.explode()
            elif node_to_split:
                node_to_split.split()

            node_to_explode = self.find_node_to_explode()
            node_to_split = self.find_node_to_split()

    def split(self):
        if type(self.left) == int and self.left > 9:
            self.left = Node([self.left//2, math.ceil(self.left/2)])
            self.left.parent = self
        elif type(self.right) == int and self.right > 9:
            self.right = Node([self.right//2, math.ceil(self.right/2)])
            self.right.parent = self

    def explode(self):
        left_node, left_side = self.find_node_with_left_regular_number()
        right_node, right_side = self.find_node_with_right_regular_number()
        if left_node:
            if left_side == 'left':
                left_node.left += self.left
            else:
                left_node.right += self.left
        if right_node:
            if right_side == 'left':
                right_node.left += self.right
            else:
                right_node.right += self.right

        if self.parent.left == self:
            self.parent.left = 0
        else:
            self.parent.right = 0

    def magnitude(self):
        if type(self.left) == int:
            left_m = self.left * 3
        else:
            left_m = self.left.magnitude() * 3

        if type(self.right) == int:
            right_m = self.right * 2
        else:
            right_m = self.right.magnitude() * 2

        return left_m + right_m

    def find_node_to_explode(self):
        S = deque([self])
        while len(S):
            n = S.popleft()
            if n.is_bottom() and n.find_depth() > 4:
                return n
            if type(n.left) == Node:
                S.append(n.left)
            if type(n.right) == Node:
                S.append(n.right)

    def find_node_to_split(self):
        if type(self.left) == int and self.left > 9:
            return self

        if type(self.left) == Node:
            left = self.left.find_node_to_split()
            if left:
                return left

        if type(self.right) == int and self.right > 9:
            return self

        if type(self.right) == Node:
            right = self.right.find_node_to_split()
            if right:
                return right

    def find_node_with_left_regular_number(self):
        prev = self
        node = self.parent
        while node and node.left == prev:
            prev = node
            node = prev.parent
        if not node:
            return None, None

        if type(node.left) == int:
            return node, 'left'
        node = node.left
        while type(node.right) != int:
            node = node.right

        while type(node.right) != int:
            node = node.right

        return node, 'right'

    def find_node_with_right_regular_number(self):
        prev = self
        node = self.parent
        while node and node.right == prev:
            prev = node
            node = prev.parent
        if not node:
            return None, None

        if type(node.right) == int:
            return node, 'right'
        node = node.right
        while type(node.left) != int:
            node = node.left

        while type(node.left) != int:
            node = node.left

        return node, 'left'

    def __repr__(self) -> str:
        return f"[{self.left},{self.right}]"


def solve1(lines):
    node = None
    left_node = Node(eval(lines[0]))
    for line in lines[1:]:
        node = Node()
        right_node = Node(eval(line))

        node.set_left(left_node)
        node.set_right(right_node)
        node.reduce()

        left_node = node

    return node.magnitude()


def solve2(lines):
    max_magnitude = 0

    node = None
    for line1 in lines:
        for line2 in lines:
            if line1 == line2:
                continue

            node1 = Node(eval(line1))
            node2 = Node(eval(line2))

            node = Node()
            node.set_left(node1)
            node.set_right(node2)

            node.reduce()

            max_magnitude = max(node.magnitude(), max_magnitude)

    return max_magnitude


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve1(lines))
        print(solve2(lines))
