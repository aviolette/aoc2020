from day5.puzzle5 import seat_id
from day5.puzzle5 import seat


def test_seat():
    assert seat("BFFFBBFRRR") == (70, 7)
    assert seat("FFFBBBFRRR") == (14, 7)
    assert seat("BBFFBBFRLL") == (102, 4)


def test_seat_id():
    assert seat_id("FBFBBFFRLR") == 357
