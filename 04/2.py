from typing import List


class Board():
    def __init__(self, board, size) -> None:
        self.board = board
        self.marks = [[0 for x in range(size)] for y in range(size)]
        self.size = size

    def mark_number(self, number) -> None:
        if number in self.board.values():
            for y in range(self.size):
                for x in range(self.size):
                    if self.board[(y, x)] == number:
                        self.marks[y][x] = 1

    def has_full_row_or_col(self) -> bool:
        # Check for full row
        for row in range(self.size):
            if sum(self.marks[row]) == self.size:
                return True

        # Check for full col
        for col in range(self.size):
            col_sum = sum([self.marks[row][col] for row in range(self.size)])
            if col_sum == self.size:
                return True

        return False

    def get_unmarked_sum(self) -> int:
        return sum([int(value) for pos, value in self.board.items() if not self.marks[pos[0]][pos[1]]])


def create_boards(lines) -> List[Board]:
    lines = [line for line in lines if line]

    boards = []
    board_size = len(lines[0].split())
    number_of_boards = len(lines) // board_size

    for board_idx in range(number_of_boards):
        board = {}
        for y, line in enumerate(lines[board_idx*board_size:board_idx*board_size+board_size]):
            for x, num in enumerate(line.split()):
                board[(y, x)] = num
        boards.append(Board(board, board_size))

    return boards


def solve(lines):
    numbers = lines[0]
    lines = lines[1:]
    boards = create_boards(lines)

    for number in numbers.split(","):
        for board in boards:
            board.mark_number(number)

        if len(boards) == 1 and boards[0].has_full_row_or_col():
            return boards[0].get_unmarked_sum() * int(number)
        else:
            boards = [board for board in boards if not board.has_full_row_or_col()]


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
        print(solve(lines))
