from typing import Tuple


def seat(crazy_seat) -> Tuple[int, int]:
    def _to_num(seat: str):
        acc = 0
        for i in range(0, len(seat)):
            exponent = len(seat) - 1 - i
            acc += pow(2, exponent) if (seat[i] == "B" or seat[i] == "R") else 0
        return acc

    return _to_num(crazy_seat[0:7]), _to_num(crazy_seat[7:10])


def seat_id(crazy_seat):
    row, column = seat(crazy_seat)
    return (row * 8) + column


def highest_boarding_pass(file_name):
    puzzle = open(file_name, "r")
    highest = 0
    for line in puzzle.readlines():
        highest = max(seat_id(line.strip()), highest)
    return highest


def my_boarding_pass(file_name):
    puzzle = open(file_name, "r")
    lines = [seat_id(line.strip()) for line in puzzle.readlines()]
    lines.sort()

    for i in range(1, len(lines) - 1):
        prev_seat = lines[i - 1]
        if lines[i] == prev_seat + 2:
            return lines[i] - 1


if __name__ == "__main__":
    print(highest_boarding_pass("puzzle5.txt"))
    print(my_boarding_pass("puzzle5.txt"))
