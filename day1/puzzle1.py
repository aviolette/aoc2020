def combo_of_2020():
    puzzle = open('puzzle.txt', 'r')
    nums = [int(line.strip()) for line in puzzle.readlines()]
    nums.sort()
    upper = len(nums)
    for i in range(0, upper):
        x = nums[i]
        for j in range(upper - 1, 0, -1):
            y = nums[j]
            if x + y > 2020:
                upper = j
            elif x + y == 2020:
                return x, y
    return None


def three_of_2020():
    puzzle = open('puzzle.txt', 'r')
    nums = [int(line.strip()) for line in puzzle.readlines()]
    nums.sort()
    upper = len(nums)
    for i in range(0, upper):
        x = nums[i]
        for j in range(0, upper):
            y = nums[j]
            for l in range(0, upper):
                z = nums[l]
                if x + y + z == 2020:
                    return x, y, z
    return None


if __name__ == '__main__':
    tup = combo_of_2020()
    print(tup)
    print(tup[0] * tup[1])
    tup = three_of_2020()
    print(tup)
    print(tup[0] * tup[1] * tup[2])
