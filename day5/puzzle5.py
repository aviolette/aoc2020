from typing import Tuple

from elves import striplines, stripsort


def seat(crazy_seat) -> Tuple[int, int]:
    def _to_num(binaryseat: str):
        return sum(
            (
                pow(2, len(binaryseat) - 1 - i)
                if (binaryseat[i] == "B" or binaryseat[i] == "R")
                else 0
            )
            for i in range(0, len(binaryseat))
        )

    return _to_num(crazy_seat[0:7]), _to_num(crazy_seat[7:10])


def seat_id(crazy_seat):
    row, column = seat(crazy_seat)
    return (row * 8) + column


def highest_boarding_pass(file_name):
    highest = 0
    for line in striplines(file_name):
        highest = max(seat_id(line), highest)
    return highest


def my_boarding_pass(file_name):
    lines = stripsort(file_name, seat_id)

    for i in range(1, len(lines) - 1):
        prev_seat = lines[i - 1]
        if lines[i] == prev_seat + 2:
            return lines[i] - 1


if __name__ == "__main__":
    print(highest_boarding_pass("puzzle5.txt"))
    print(my_boarding_pass("puzzle5.txt"))
