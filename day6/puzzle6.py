def anyone_answers(file_name: str):
    puzzle = open(file_name, "r")
    group = set()
    groups = []
    for line in puzzle.readlines():
        line = line.strip()
        if len(line):
            for answer in line:
                group.add(answer)
        else:
            groups.append(group)
            group = set()
    if group:
        groups.append(group)
    return groups


def sum_of_answers(file_name: str):
    acc = 0
    for group in anyone_answers(file_name):
        acc += len(group)
    return acc


if __name__ == "__main__":
    print(sum_of_answers("example6.txt"))
    print(sum_of_answers("puzzle6.txt"))
