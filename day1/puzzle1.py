from functools import reduce
from typing import List

from elves import striplines, stripsort


def combo_of_2020(nums: List[int]):
    upper = len(nums)
    for i in range(0, upper):
        x = nums[i]
        for j in range(upper - 1, i, -1):
            y = nums[j]
            if x + y > 2020:
                upper = j
            elif x + y == 2020:
                return x, y
    return None


def three_of_2020(nums: List[int]):
    upper = len(nums)
    for i in range(0, upper):
        x = nums[i]
        for j in range(i, upper):
            y = nums[j]
            for l in range(j, upper):
                z = nums[l]
                if x + y + z == 2020:
                    return x, y, z
    return None


def multiple_of_2020(file_name):
    tup = combo_of_2020(stripsort(file_name, int))
    return tup[0] * tup[1]


def multiples_of_three_of_2020(file_name):
    tup = three_of_2020(stripsort(file_name, int))
    return reduce(lambda x, y: x * y, tup)


if __name__ == "__main__":
    print(multiple_of_2020("puzzle.txt"))
    print(multiples_of_three_of_2020("puzzle.txt"))
