from functools import reduce
from typing import List


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


if __name__ == "__main__":
    puzzle = open("puzzle.txt", "r")
    nums = [int(line.strip()) for line in puzzle.readlines()]
    nums.sort()

    tup = combo_of_2020(nums)
    print(tup)
    print(tup[0] * tup[1])
    tup = three_of_2020(nums)
    print(tup)
    print(reduce(lambda x, y: x * y, tup))
