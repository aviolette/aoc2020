from functools import partial

from elves import group_lines


def to_set(line):
    return {l for l in line}


def string_set(group):
    for item in group:
        yield to_set(item)


def anyone_answers(group):
    answer = set()
    for item in string_set(group):
        answer = item.union(answer)
    return answer


def everyone_answers(group):
    answer = None
    for item in string_set(group):
        if answer is None:
            answer = item
        else:
            answer = answer.intersection(item)
    return answer


def sum_of_answers(func, file_name: str):
    return sum(len(func(group)) for group in group_lines(file_name))


everyone = partial(sum_of_answers, everyone_answers)
anyone = partial(sum_of_answers, anyone_answers)

if __name__ == "__main__":
    print(anyone("example6.txt"))
    print(anyone("puzzle6.txt"))
    print(everyone("example6.txt"))
    print(everyone("puzzle6.txt"))
