from day13.puzzle13 import puzzle_two_as_list


def test_puzzle_two_example1():
    assert puzzle_two_as_list([17, "x", 13, 19]) == 3417


def test_puzzle_two_example2():
    assert puzzle_two_as_list([67, 7, 59, 61]) == 754018


def test_puzzle_two_example3():
    assert puzzle_two_as_list([67, "x", 7, 59, 61]) == 779210


def test_puzzle_two_example4():
    assert puzzle_two_as_list([67, 7, "x", 59, 61]) == 1261476


def test_puzzle_two_example5():
    assert puzzle_two_as_list([1789, 37, 47, 1889]) == 1202161486
