from elves import striplines


class Bag:
    def __init__(self, name: str, amount: int, children):
        self.name = name
        self.amount = amount
        self.children = children

    def __repr__(self):

        return f"Bag({self.name}, {self.amount}, [{', '.join(map(lambda x: repr(x), self.children))}]"


def parse_bags(file_name):
    for line in striplines(file_name):
        words = line.split()
        children = (
            []
            if words[4] == "no"
            else [
                Bag(words[i + 1] + " " + words[i + 2], int(words[i]), [])
                for i in range(4, len(words), 4)
            ]
        )
        bag = Bag(words[0] + " " + words[1], 1, children)
        yield bag


def _can_contain(bag_name, bag, bags, member):
    if bag_name == bag.name:
        return True
    if bag_name in member:
        return False
    member.add(bag.name)
    for child in bag.children:
        child_bag = bags.get(child.name)
        if _can_contain(bag_name, child_bag, bags, member):
            return True
    return False


def can_contain(bag_name, bag, bags):
    return _can_contain(bag_name, bag, bags, set())


def bag_combos(file_name, bag_name):
    bags = get_bags(file_name)
    acc = 0
    for _, bag in bags.items():
        if bag.name == bag_name:
            continue
        acc += 1 if can_contain(bag_name, bag, bags) else 0
    return acc


def get_bags(file_name):
    bags = {}
    for bag in parse_bags(file_name):
        bags[bag.name] = bag
    return bags


def descend_count(the_bag, bags):
    acc = 1
    for bag in the_bag.children:
        amount = bag.amount
        child = bags.get(bag.name)
        if amount > 0:
            count = descend_count(child, bags)
            print(f"{count} {child.name} bags")
            acc += amount * count
    return acc


def num_bags(file_name, bag_name):
    bags = get_bags(file_name)
    the_bag = bags.get(bag_name)
    return descend_count(the_bag, bags) - 1


if __name__ == "__main__":
    #    print(bag_combos("example7.txt", "shiny gold"))
    #    print(bag_combos("puzzle7.txt", "shiny gold"))
    print(num_bags("example7.txt", "shiny gold"))
    print(num_bags("example71.txt", "shiny gold"))
    print(num_bags("puzzle7.txt", "shiny gold"))
