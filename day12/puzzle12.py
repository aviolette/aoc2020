from elves import striplines

ANGLES = {"E": 0, "W": 180, "S": 270, "N": 90}


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


def scalar_multiply(scalar, vector):
    return [scalar * v_i for v_i in vector]


def vector_multiply(v1, v2):
    return [v_1 * v_2 for v_1, v_2 in zip(v1, v2)]


def vector_rotate(vector, angle):
    # theta = math.radians(angle)
    #
    # cs = math.cos(theta)
    # sn = math.sin(theta)
    #
    # return [
    #     greater(vector[0] * cs - vector[1] * sn),
    #     greater(vector[0] * sn + vector[1] * cs),
    # ]
    x, y = vector
    if angle == 90 or angle == -270:
        return [-y, x]
    elif angle == -90 or angle == 270:
        return [y, -x]
    elif angle == 180 or angle == -180:
        return [-x, -y]
    raise Exception("Foo")


def manhattan_distance_with_waypoint(file_name):
    waypoint = [10, 1]
    pos = [0, 0]
    for instruction, value in instructions(file_name):
        if instruction == "F":
            move = scalar_multiply(value, waypoint)
            pos = vector_add(pos, move)
        elif instruction == "R":
            waypoint = vector_rotate(waypoint, -value)
        elif instruction == "L":
            waypoint = vector_rotate(waypoint, value)
        else:
            tmp_angle = ANGLES[instruction]
            v = vector_from_direction(value, tmp_angle)
            waypoint = vector_add(v, waypoint)
    return sum([abs(x) for x in pos])


if __name__ == "__main__":
    #    print(manhattan_distance("puzzle12.txt"))
    print(vector_rotate([10, 4], -90))
    print(manhattan_distance_with_waypoint("puzzle12.txt"))
