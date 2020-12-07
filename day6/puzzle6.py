from functools import partial


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


def everyone_answers(file_name):
    puzzle = open(file_name, "r")
    group = set()
    group_start = True
    groups = []
    for line in puzzle.readlines():
        line = line.strip()
        if len(line):
            person = set()
            for answer in line:
                person.add(answer)
            if group:
                group = group.intersection(person)
            elif group_start:
                group = person
            group_start = False
        else:
            group_start = True
            groups.append(group)
            group = set()
    if group:
        groups.append(group)
    return groups


def sum_of_answers(func, file_name: str):
    acc = 0
    for group in func(file_name):
        acc += len(group)
    return acc


everyone = partial(sum_of_answers, everyone_answers)
anyone = partial(sum_of_answers, anyone_answers)

if __name__ == "__main__":
    print(anyone("example6.txt"))
    print(anyone("puzzle6.txt"))
    print(everyone("example6.txt"))
    print(everyone("puzzle6.txt"))
