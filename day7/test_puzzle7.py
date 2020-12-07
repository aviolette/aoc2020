from day7.puzzle7 import bag_combos, num_bags


def test_bag_combos():
    assert bag_combos("example7.txt", "shiny gold") == 4


def test_bag_combos2():
    assert bag_combos("puzzle7.txt", "shiny gold") == 192


def test_num_bags():
    assert num_bags("example7.txt", "shiny gold") == 32


def test_num_bags2():
    assert num_bags("example71.txt", "shiny gold") == 126


def test_num_bags3():
    assert num_bags("puzzle7.txt", "shiny gold") == 12128
