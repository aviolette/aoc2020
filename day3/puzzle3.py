import math
from functools import reduce


def expand_line(line, position):
    line = line.strip()
    return line * math.ceil((position + 1) / len(line))


def compute_trees(lines, right, down):
    tree_count = 0
    position = 0
    down_counter = down
    for line in lines:
        if down_counter != down:
            down_counter += 1
            continue
        down_counter = 1
        real_line = expand_line(line, position)
        if real_line[position] == "#":
            tree_count += 1
        position += right
    return tree_count


def compute_trees_from_file(file_name):
    puzzle = open(file_name, "r")
    return compute_trees([line for line in puzzle.readlines()], right=3, down=1)


def product_of_all_slopes(file_name):
    puzzle = open(file_name, "r")
    lines = [line for line in puzzle.readlines()]

    return reduce(
        lambda x, y: x * y,
        (
            compute_trees(lines, right=1, down=1),
            compute_trees(lines, right=3, down=1),
            compute_trees(lines, right=5, down=1),
            compute_trees(lines, right=7, down=1),
            compute_trees(lines, right=1, down=2),
        ),
    )


if __name__ == "__main__":
    print(compute_trees_from_file("example.txt"))
    print(compute_trees_from_file("puzzle3.txt"))
    print(product_of_all_slopes("example.txt"))
    print(product_of_all_slopes("puzzle3.txt"))
