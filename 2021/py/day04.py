import sys


def parse_data(filename):
    with open(filename) as file:
        data = file.read().split("\n\n")

    numbers = [int(n) for n in data[0].split(",")]
    boards = data[1:]

    boards = [board.splitlines() for board in boards]

    boards = [
        [row.strip().replace("  ", " ").split(" ") for row in board] for board in boards
    ]

    boards = [[[int(n) for n in row] for row in board] for board in boards]

    return numbers, boards


def check_number_in_board(number, board):
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if number == col:
                return (x, y)
    return "nope", "nope"


def make_empty_five_by_five():
    return [[0 for _ in range(5)] for _ in range(5)]


class ScoreTable:
    def __init__(self, num_boards):
        self.num_boards = num_boards
        self.scores = self.make_score_table()

    def make_score_table(self):
        return [make_empty_five_by_five() for _ in range(self.num_boards)]

    def update_scores(self, number, boards):
        assert len(boards) == self.num_boards
        for i, board in enumerate(boards):
            x, y = check_number_in_board(number, board)
            if x != "nope":
                self.scores[i][y][x] = 1

    def check_for_winning_boards(self):
        winners = set()
        for i, scores in enumerate(self.scores):
            if 5 in [sum(row) for row in scores]:
                winners.add(i)
            if 5 in [sum(col) for col in zip(*scores)]:
                winners.add(i)
        return winners


def sum_unmarked_numbers_on_board(board, scores):
    total = 0
    for y in range(5):
        for x in range(5):
            if scores[y][x] == 0:
                total += board[y][x]
    return total


def main(filename):
    """B-I-N-G-O
    TODO:
        check each board for number
        update status
        check for winning row/column
        sum winning board's unmarked numbers
        mulitply sum by winning number
    """
    numbers, boards = parse_data(filename)
    score_table = ScoreTable(len(boards))
    numbers_checked = []

    def step(numbers, score_table, boards):
        num = numbers.pop(0)
        numbers_checked.append(num)
        score_table.update_scores(num, boards)
        return score_table.check_for_winning_boards()

    winners = None
    while not winners:
        winners = step(numbers, score_table, boards)

    winner = winners.pop()
    winners.add(winner)
    unmarked = sum_unmarked_numbers_on_board(boards[winner], score_table.scores[winner])
    print("Part One:")
    print(unmarked * numbers_checked[-1])

    while len(winners) < (len(boards) - 1):
        winners = step(numbers, score_table, boards)

    board_index_set = set(range(len(boards)))
    last_board = board_index_set.difference(winners).pop()

    while len(winners) < len(boards):
        winners = step(numbers, score_table, boards)

    unmarked = sum_unmarked_numbers_on_board(
        boards[last_board], score_table.scores[last_board]
    )

    print("Part Two:")
    print(unmarked * numbers_checked[-1])


if __name__ == "__main__":
    main(sys.argv[1])
