import math


def expand_line(line, position):
    line = line.strip()
    return line * max(math.ceil((position + 1) / len(line)), 1)


def compute_trees(lines):
    tree_count = 0
    position = 0
    for line in lines:
        real_line = expand_line(line, position)
        if real_line[position] == "#":
            tree_count += 1
        position += 3
    return tree_count


def compute_trees_from_file(file_name):
    puzzle = open(file_name, "r")
    lines = [line for line in puzzle.readlines()]
    return compute_trees(lines)


if __name__ == "__main__":
    print(compute_trees_from_file("example.txt"))
    print(compute_trees_from_file("puzzle3.txt"))
