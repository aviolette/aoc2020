from elves import intlines, striplines


def sum_set(preamble):
    return {x + y for x in preamble for y in preamble}


def first_non_sum_of_preamble(file_name, preamble_size):
    puzzle = [line for line in intlines(file_name)]
    for i in range(preamble_size, len(puzzle)):
        solutions = sum_set(puzzle[i - preamble_size : i])
        if puzzle[i] not in solutions:
            return puzzle[i]
    return None


if __name__ == "__main__":
    print(first_non_sum_of_preamble("example9.txt", 5))
    print(first_non_sum_of_preamble("puzzle9.txt", 25))
    # 776203571
