from day2.puzzle2 import Rule, SecondRule


def test_verify():
    rule = Rule("9-13 p")
    assert rule.verify("bppxpjpmpwcpppdprpp")


def test_verify_below():
    rule = Rule("7-11 l")
    assert not rule.verify("llllll")


def test_verify_at_lower():
    rule = Rule("7-11 l")
    assert rule.verify("lllllll")


def test_verify_at_upper():
    rule = Rule("7-11 l")
    assert rule.verify("lllllllllll")


def test_verify_above_upper():
    rule = Rule("7-11 l")
    assert not rule.verify("llllllllllll")


def test_verify_rule_2_not():
    rule = SecondRule("1-6 w")
    assert not rule.verify("dwnwws")


def test_verify_rule_2_pos1():
    rule = SecondRule("1-6 w")
    assert rule.verify("wwnwws")


def test_verify_rule_2_pos2():
    rule = SecondRule("1-6 w")
    assert rule.verify("dwnwww")
