
class DeterministicDie:
    def __init__(self):
        self.prev_roll = 0
        self.rolls = 0

    def roll(self):
        self.prev_roll += 1
        if self.prev_roll > 100:
            self.prev_roll = 1
        self.rolls += 1
        return self.prev_roll


class Player:
    def __init__(self, start_pos: int, target_score: int):
        self.pos = start_pos
        self.score = 0
        self.target_score = target_score
        pass

    def __repr__(self) -> str:
        return f"pos: {self.pos}, score: {self.score}"

    def take_turn(self, die: DeterministicDie):
        steps = 0
        for _ in range(3):
            steps += die.roll()
        steps %= 10
        self.pos += steps
        if self.pos > 10:
            self.pos -= 10
        self.score += self.pos

    def has_won(self):
        return self.score >= self.target_score


def solve1(lines):
    die = DeterministicDie()
    player1 = Player(int(lines[0].split(' ')[-1]), 1000)
    player2 = Player(int(lines[1].split(' ')[-1]), 1000)

    while True:
        player1.take_turn(die)
        if player1.has_won():
            return die.rolls * player2.score

        player2.take_turn(die)
        if player2.has_won():
            return die.rolls * player1.score


def game(p1_pos, p2_pos, p1_score, p2_score, dp):
    initial_state = p1_pos, p2_pos, p1_score, p2_score

    if initial_state in dp:
        return dp[initial_state]

    if p1_score >= 21:
        return [1, 0]
    if p2_score >= 21:
        return [0, 1]

    winners = [0, 0]

    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                new_p1_pos = (p1_pos + i + j + k - 1) % 10 + 1
                new_p1_score = p1_score + new_p1_pos
                sub_winners = game(p2_pos, new_p1_pos, p2_score, new_p1_score, dp)
                winners = [winners[0] + sub_winners[1], winners[1] + sub_winners[0]]

    dp[initial_state] = winners

    return winners


def solve2(lines):
    return max(game(int(lines[0].split(' ')[-1]), int(lines[1].split(' ')[-1]), 0, 0, {}))


if __name__ == "__main__":
    with open('./input', 'r') as f:
        lines = f.read().splitlines()

        print(solve1(lines))
        print(solve2(lines))
