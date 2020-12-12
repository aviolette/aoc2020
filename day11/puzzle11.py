from collections import Counter
from copy import deepcopy

from elves import striplines


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end="")
        print("")


def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def adjacents(matrix, i, j):
    return Counter(
        [
            matrix[x][y]
            for x in range(max(i - 1, 0), min(len(matrix), i + 2))
            for y in range(max(j - 1, 0), min(len(matrix[x]), j + 2))
            if x != i or y != j
        ]
    )


def progress(matrix, i, j, max_count, pos_func):
    count = 0
    inc = 0
    while True:
        x, y = pos_func(matrix, i, j, inc)
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return count
        if (x, y) == (i, j):
            pass
        elif matrix[x][y] == "L":
            return count
        elif matrix[x][y] == "#":
            count = count + 1
            return count
        inc = inc + 1


def seats_in_line_of_site(matrix, i, j, max_seats):
    directions = [
        lambda m, row, col, inc: (row + inc, col + inc),  # southeast
        lambda m, row, col, inc: (row + inc, col - inc),  # southwest
        lambda m, row, col, inc: (row - inc, col + inc),  # northeast
        lambda m, row, col, inc: (row - inc, col - inc),  # northwest
        lambda m, row, col, inc: (row - inc, col),  # north
        lambda m, row, col, inc: (row + inc, col),  # south
        lambda m, row, col, inc: (row, col + inc),  # east
        lambda m, row, col, inc: (row, col - inc),  # west
    ]
    count = 0
    for direction in directions:
        count += progress(matrix, i, j, max_seats, direction)
        if count >= max_seats:
            break
    return count


def line_of_site2(matrix, i, j, nw, north, ne, east):
    key = f"{i},{j}"
    north_val = Counter()
    east_val = Counter()
    nw_val = Counter()
    ne_val = Counter()
    if str(j) not in north:
        north_val = north[str(j)] = Counter([row[j] for row in matrix])
    if str(i) not in east:
        east_val = east[str(i)] = Counter([col for col in matrix[i]])
    if key not in nw:
        key_set = []
        value_set = []
        row = 0
        for col in range(j, len(matrix[0])):
            if col < 0 or row < 0:
                continue
            key_set.append(f"{row},{col}")
            value_set.append(matrix[row][col])
            row = row + 1
        counter = Counter(value_set)
        for key in key_set:
            nw[key] = counter
    if key not in ne:
        key_set = []
        value_set = []
        row = 0
        for col in range(j + i, -1, -1):
            if row < 0:
                break
            if col < 0 or col >= len(matrix[0]):
                continue
            key_set.append(f"{row},{col}")
            value_set.append(matrix[row][col])
            row = row + 1
        counter = Counter(value_set)
        for key in key_set:
            nw[key] = counter
    return north_val + east_val + nw_val + ne_val


def puzzle11_two(file_name):
    lines = [line for line in striplines(file_name)]
    matrix = make_matrix(len(lines), len(lines[0]), lambda i, j: lines[i][j])
    while True:
        nw = {}
        north = {}
        ne = {}
        east = {}
        matrix2 = deepcopy(matrix)
        occupied_seats = 0
        for i in range(0, len(matrix2)):
            for j in range(0, len(matrix2[i])):
                touched = False
                if matrix[i][j] == "L":
                    count = seats_in_line_of_site(matrix, i, j, 1)
                    if count == 0:
                        matrix2[i][j] = "#"
                        occupied_seats = occupied_seats + 1
                        touched = True
                elif matrix[i][j] == "#":
                    count = seats_in_line_of_site(matrix, i, j, 5)
                    if count >= 5:
                        matrix2[i][j] = "L"
                        touched = True
                        occupied_seats = occupied_seats - 1
                if not touched:
                    occupied_seats += 1 if (matrix[i][j] == "#") else 0
        print_matrix(matrix)
        print(" ")
        if matrix2 == matrix:
            break
        else:
            matrix = matrix2
    print(bool(matrix == matrix2))
    print(occupied_seats)
    return matrix2


def puzzle11_one(file_name):
    lines = [line for line in striplines(file_name)]
    matrix = make_matrix(len(lines), len(lines[0]), lambda i, j: lines[i][j])
    while True:
        matrix2 = deepcopy(matrix)
        occupied_seats = 0
        for i in range(0, len(matrix2)):
            for j in range(0, len(matrix2[i])):
                touched = False
                if matrix[i][j] == "L":
                    items = adjacents(matrix, i, j)
                    if items["#"] == 0:
                        matrix2[i][j] = "#"
                        occupied_seats = occupied_seats + 1
                        touched = True
                elif matrix[i][j] == "#":
                    items = adjacents(matrix, i, j)
                    if items["#"] >= 4:
                        matrix2[i][j] = "L"
                        touched = True
                        occupied_seats = occupied_seats - 1
                if not touched:
                    occupied_seats += 1 if (matrix[i][j] == "#") else 0
        if matrix2 == matrix:
            break
        else:
            matrix = matrix2
    print(bool(matrix == matrix2))
    print_matrix(matrix)
    print(occupied_seats)
    return matrix2


if __name__ == "__main__":
    #    puzzle11_one("example.txt")
    # puzzle11_one("puzzle11.txt")
    # puzzle11_two("example.txt")
    puzzle11_two("puzzle11.txt")
    baz = [
        ["#", ".", "#", "#", ".", "#", "#", ".", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", ".", "#", "#"],
        ["#", ".", "#", ".", "#", ".", ".", "#", ".", "."],
        ["#", "#", "#", "#", ".", "#", "#", ".", "#", "#"],
        ["#", ".", "#", "#", ".", "#", "#", ".", "#", "#"],
        ["#", ".", "#", "#", "#", "#", "#", ".", "#", "#"],
        [".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", "#", "#", "#", "#", "#", "#", ".", "#"],
        ["#", ".", "#", "#", "#", "#", "#", ".", "#", "#"],
    ]
    # print(seats_in_line_of_site(baz, 0, 0, 5))
