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


class SecondRule:
    def __init__(self, definition: str):
        char_range, the_char = definition.split(" ")
        self.pos1, self.pos2 = (
            int(x.strip()) - 1 for x in char_range.strip().split("-")
        )
        self.the_char = the_char

    def verify(self, password):
        return (password[self.pos1] == self.the_char) != (
            password[self.pos2] == self.the_char
        )


def count_valid_passwords(puzzle, rule_class):
    count = 0
    for line in lines:
        rule_spec, password = line.split(":")
        rule = rule_class(rule_spec.strip())
        if rule.verify(password.strip()):
            count = count + 1
    return count


if __name__ == "__main__":
    puzzle = open("puzzle2.txt", "r")
    lines = [line for line in puzzle.readlines()]
    print(count_valid_passwords(lines, Rule))
    print(count_valid_passwords(lines, SecondRule))
