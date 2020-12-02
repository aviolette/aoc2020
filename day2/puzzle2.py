from collections import Counter


class Rule:
    def __init__(self, definition: str):
        char_range, the_char = definition.split(" ")
        self.lower, self.upper = (int(x.strip()) for x in char_range.strip().split("-"))
        self.the_char = the_char

    def verify(self, password):
        counter = Counter(password)
        count = counter.get(self.the_char, 0)
        return self.lower <= count <= self.upper


def count_valid_passwords(puzzle):
    count = 0
    for line in puzzle.readlines():
        rule_spec, password = line.split(":")
        rule = Rule(rule_spec.strip())
        if rule.verify(password.strip()):
            count = count + 1
    return count


if __name__ == "__main__":
    puzzle = open("puzzle2.txt", "r")
    print(count_valid_passwords(puzzle))
