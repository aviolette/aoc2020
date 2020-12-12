from elves import striplines


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def instructions(file_name):
    for line in striplines(file_name):
        yield line[0], int(line[1:])


def vector_from_direction(value, angle):
    if angle == 0:
        return [value, 0]
    if angle == 90:
        return [0, value]
    if angle == 270:
        return [0, -value]
    if angle == 180:
        return [-value, 0]


def manhattan_distance(file_name):
    pos = [0, 0]
    facing_angle = 0
    for instruction, value in instructions(file_name):
        tmp_angle = facing_angle
        if instruction == "R":
            facing_angle = facing_angle - value
            if facing_angle >= 360 or facing_angle < 0:
                facing_angle = facing_angle % 360
            continue
        elif instruction == "L":
            facing_angle = facing_angle + value
            if facing_angle >= 360 or facing_angle < 0:
                facing_angle = facing_angle % 360
            continue
        elif instruction == "N":
            tmp_angle = 90
        elif instruction == "E":
            tmp_angle = 0
        elif instruction == "W":
            tmp_angle = 180
        elif instruction == "S":
            tmp_angle = 270
        v = vector_from_direction(value, tmp_angle)
        pos = vector_add(v, pos)
    return sum([abs(x) for x in pos])


if __name__ == "__main__":
    print(manhattan_distance("puzzle12.txt"))
