from elves import striplines


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
    numeric_ids = [int(bus) for bus in bus_ids if bus != "x"]
    timestamp = 0
    candidate = 0
    step = numeric_ids[0]

    max_index = 0
    max_bus = 0
    for i, bus in enumerate(bus_ids):
        if bus == "x":
            continue
        if not max_bus or int(bus) > max_bus:
            max_bus = int(bus)
            max_index = i
    step = max_bus
    candidate = 0
    while True:
        if in_alignment(bus_ids, candidate - max_index):
            break
        candidate += step
        print(candidate)
    return candidate - max_index


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
    # print(puzzle_two("example13.txt"))
    # print(puzzle_two("example131.txt"))
    # print(puzzle_two("example132.txt"))
    # print(puzzle_two("example133.txt"))
    print(puzzle_two("puzzle13.txt"))
