from collections import defaultdict

from elves import intlines


def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def descend(i, tree, stats, tup):
    if not tree[i]:
        return 1

    acc = 0
    for child in tree[i]:
        if child in stats:
            acc += stats[child]
        else:
            stats[child] = descend(child, tree, stats, tup + (child,))
            acc += stats[child]
    return acc


def puzzle_two_two(file_name):
    lines = [line for line in intlines(file_name)]
    lines.sort()
    tree = defaultdict(lambda: list())
    for i in range(0, len(lines)):
        j = 1
        value = lines[i]
        while j <= 3 and i + j < len(lines) and lines[j + i] - value <= 3:
            tree[value].append(lines[i + j])
            j += 1
    baz = {}
    acc = 0
    for i in range(1, 4):
        if i in tree:
            acc += descend(i, tree, baz, ())
    print(acc)


def puzzle_one(file_name):
    lines = [line for line in intlines(file_name)]
    lines.sort()
    last = 0
    diffs = [0, 0, 0]
    for joltage in lines:
        diff = joltage - last
        diffs[diff - 1] = diffs[diff - 1] + 1
        last = joltage
    diffs[2] = diffs[2] + 1
    return (diffs[0], (diffs[2]))


if __name__ == "__main__":
    #    print(puzzle_one("example1.txt"))
    #    print(puzzle_one("example2.txt"))
    # tup = puzzle_one("puzzle10.txt")
    # print(tup)
    # print(tup[0] * tup[1])
    puzzle_two_two("example2.txt")
    puzzle_two_two("puzzle10.txt")
