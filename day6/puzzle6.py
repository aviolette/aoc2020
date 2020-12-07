from functools import partial


def anyone_answers(person: str, group: set):
    if group is None:
        group = set()
    for answer in person:
        group.add(answer)
    return group


def everyone_answers(person: str, group: set):
    person_answers = {answer for answer in person}
    if group:
        return group.intersection(person_answers)
    elif group is None:
        return person_answers
    return set()


def sum_of_answers(func, file_name: str):
    puzzle = open(file_name, "r")
    group = None
    acc = 0
    for line in puzzle.readlines():
        line = line.strip()
        if len(line):
            group = func(line, group)
        else:
            acc += len(group)
            group = None

    return len(group) + acc


everyone = partial(sum_of_answers, everyone_answers)
anyone = partial(sum_of_answers, anyone_answers)

if __name__ == "__main__":
    print(anyone("example6.txt"))
    print(anyone("puzzle6.txt"))
    print(everyone("example6.txt"))
    print(everyone("puzzle6.txt"))
