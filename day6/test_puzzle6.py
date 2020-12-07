from day6.puzzle6 import anyone, everyone


def test_everyone():
    assert everyone("example6.txt") == 6
    assert everyone("puzzle6.txt") == 3402


def test_anyone():
    assert anyone("example6.txt") == 11
    assert anyone("puzzle6.txt") == 6534
