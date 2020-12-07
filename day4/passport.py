import re

from elves import group_lines, striplines

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def vali_date(value, lower, upper) -> bool:
    if len(value) != 4:
        return False
    return lower <= int(value) <= upper


def validate_height(value) -> bool:
    m = re.search("([0-9]+)(in|cm)", value)
    if m:
        if m.group(2) == "in":
            return 59 <= int(m.group(1)) <= 76
        else:
            return 150 <= int(m.group(1)) <= 193
    return False


def validate_haircolor(value) -> bool:
    if len(value) != 7:
        return False
    if value[0] != "#":
        return False
    return bool(re.search("([a-f]|[0-9]){6}", value[1:7]))


def validate_passport_id(value):
    return bool(re.search("^[0-9]{9}$", value))


def validate(field, value) -> bool:
    if "byr" == field:
        return vali_date(value, 1920, 2002)
    elif "iyr" == field:
        return vali_date(value, 2010, 2020)
    elif "eyr" == field:
        return vali_date(value, 2020, 2030)
    elif "hgt" == field:
        return validate_height(value)
    elif "hcl" == field:
        return validate_haircolor(value)
    elif "ecl" == field:
        return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    elif "pid" == field:
        return validate_passport_id(value)
    return True


def is_valid(passport_data):
    passport_fields = passport_data.strip().split(" ")
    fields = {field.split(":")[0] for field in passport_fields}
    has_fields = REQUIRED_FIELDS.issubset(fields)
    if not has_fields:
        return False
    return all(validate(*field.split(":")) for field in passport_fields)


def valid_passports(file_name):
    return sum(
        1 if is_valid(" ".join(group)) else 0 for group in group_lines(file_name)
    )


if __name__ == "__main__":
    print(valid_passports("example.txt"))
    print(valid_passports("puzzle4.txt"))
