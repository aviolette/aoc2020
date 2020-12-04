from day4.passport import validate_haircolor, validate_height


def test_validate_height_cm_lowest():
    assert validate_height("150cm")


def test_validate_height_cm_lower():
    assert not validate_height("149cm")


def test_validate_height_cm_highest():
    assert validate_height("193cm")


def test_validate_height_cm_higher():
    assert not validate_height("194cm")


def test_validate_height_in_lowest():
    assert validate_height("59in")


def test_validate_height_in_lower():
    assert not validate_height("58in")


def test_validate_height_in_highest():
    assert validate_height("76in")


def test_validate_height_in_higher():
    assert not validate_height("77in")


def test_validate_haircolor():
    assert not validate_haircolor("z")


def test_validate_haircolor1():
    assert not validate_haircolor("#ade3")


def test_validate_haircolor2():
    assert validate_haircolor("#aaff12")
