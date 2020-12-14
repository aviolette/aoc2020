from elves import striplines

from functools import reduce


# next two functions ripped off from internet: https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 0
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def in_alignment(bus_ids, timestamp):
    for i, bus in enumerate(bus_ids):
        if bus == "x":
            continue
        bus = int(bus)
        wait_time = bus - (timestamp % bus)
        if wait_time == bus:
            wait_time = 0
        if wait_time != i:
            return False
    return True


def puzzle_two_as_list(bus_ids):
    numeric_ids = [float(bus) for bus in bus_ids if bus != "x"]

    remainders = []
    for i, item in enumerate(bus_ids):
        if item == "x":
            continue
        remainders.append(-float(i))
    return chinese_remainder(numeric_ids, remainders)


def puzzle_two(file_name):
    _, bus_ids = striplines(file_name)
    bus_ids = bus_ids.split(",")
    return puzzle_two_as_list(bus_ids)


def puzzle_one(file_name):
    timestamp, bus_ids = striplines(file_name)
    bus_ids = [int(bus) for bus in bus_ids.split(",") if bus != "x"]
    timestamp = int(timestamp)
    chosen_bus = None
    smallest_time = None

    for bus in bus_ids:
        wait_time = bus - (timestamp % bus)
        if not smallest_time or wait_time < smallest_time:
            smallest_time = wait_time
            chosen_bus = bus

    return chosen_bus * smallest_time


if __name__ == "__main__":
    # print(puzzle_one("example13.txt"))
    # print(puzzle_one("puzzle13.txt"))
    #    print(in_alignment([7, 13, "x", "x", 59, "x", 31, 19], 1068781))
    #    print(puzzle_two("example13.txt"))
    # print(puzzle_two("example131.txt"))
    # print(puzzle_two("example132.txt"))
    #    print(puzzle_two("example133.txt"))
    print(chinese_remainder([17.0, 13.0, 19.0], [-0.0, -2.0, -3.0]))
    print(
        chinese_remainder(
            [17.0, 37.0, 571.0, 13.0, 23.0, 29.0, 401.0, 41.0, 19.0],
            [0.0, -11.0, -17.0, -35.0, -40.0, -46.0, -48.0, -58.0, -67.0],
        )
    )
    print(puzzle_two("puzzle13.txt"))
    print(
        in_alignment(
            [
                "17",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "37",
                "x",
                "x",
                "x",
                "x",
                "x",
                "571",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "13",
                "x",
                "x",
                "x",
                "x",
                "23",
                "x",
                "x",
                "x",
                "x",
                "x",
                "29",
                "x",
                "401",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "41",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "x",
                "19",
            ],
            226845233210288,
        )
    )
#    print(chinese_remainder([17, 13, 19], [0, -2, -3]))
