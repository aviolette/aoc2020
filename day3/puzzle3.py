from functools import reduce

from elves import striplines


def compute_trees(lines, right, down):
    tree_count = 0
    position = 0
    down_counter = down
    for line in lines:
        if down_counter != down:
            down_counter += 1
            continue
        down_counter = 1
        offset = position % len(line)
        if line[offset] == "#":
            tree_count += 1
        position += right
    return tree_count


def compute_trees_from_file(file_name):
    return compute_trees([line for line in striplines(file_name)], right=3, down=1)


def product_of_all_slopes(file_name):
    lines = [line for line in striplines(file_name)]

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
