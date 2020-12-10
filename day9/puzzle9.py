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


def sum_of_at_least_two_equals(what, file_name):
    puzzle = [line for line in intlines(file_name)]
    for tup_size in range(2, len(puzzle)):
        for i in range(0, len(puzzle) - tup_size):
            candidate = puzzle[i : i + tup_size]
            if sum(candidate) == what:
                candidate.sort()
                return (
                    candidate[0],
                    candidate[tup_size - 1],
                    candidate[0] + candidate[tup_size - 1],
                )
    return None


if __name__ == "__main__":
    # print(first_non_sum_of_preamble("example9.txt", 5))
    # print(first_non_sum_of_preamble("puzzle9.txt", 25))
    # 776203571
    # print(sum_of_at_least_two_equals(127, "example9.txt"))
    print(sum_of_at_least_two_equals(776203571, "puzzle9.txt"))
    # (27369156, 77431413, 104800569)
