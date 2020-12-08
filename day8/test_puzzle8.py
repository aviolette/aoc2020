from day8.puzzle8 import find_acc_value, find_bad_boot_code


def test_find_acc_value():
    assert find_acc_value("example8a.txt") == 5


def test_find_acc_value2():
    assert find_acc_value("puzzle8.txt") == 1594


def test_find_bad_boot_code():
    assert find_bad_boot_code("example8a.txt") == 8


def test_find_bad_boot_code2():
    assert find_bad_boot_code("puzzle8.txt") == 758
