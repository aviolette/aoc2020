from collections import defaultdict


class FirstSecond:
    def __init__(self):
        self._current = None
        self.last = None

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self.last = self._current
        self._current = value

    def diff(self):
        return self._current - self.last

    def is_new(self):
        return self.last is None


def puzzle_one(input, max_turns):
    items = defaultdict(lambda: FirstSecond())
    spoken = -1
    for turn in range(0, max_turns):
        if turn < len(input):
            spoken = input[turn]
        elif items[spoken].is_new():
            spoken = 0
        else:
            spoken = items[spoken].diff()
        items[spoken].current = turn

    return spoken


if __name__ == "__main__":
    example1 = [0, 3, 6]
    #    print(puzzle_one([0, 3, 6], 10))
    # print(puzzle_one([1, 3, 2], 2020))
    # print(puzzle_one([2, 1, 3], 2020))
    # print(puzzle_one([1, 2, 3], 2020))
    # print(puzzle_one([2, 3, 1], 2020))
    # print(puzzle_one([3, 1, 2], 2020))
    print(puzzle_one([1, 0, 18, 10, 19, 6], 30000000))
#    puzzle_input = [1, 0, 18, 10, 19, 6]
