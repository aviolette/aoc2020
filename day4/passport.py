REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def is_valid(passport_data):
    passport_fields = passport_data.strip().split(" ")
    fields = {field.split(":")[0] for field in passport_fields}
    return REQUIRED_FIELDS.issubset(fields)


def valid_passports(file_name):
    puzzle = open(file_name, "r")
    acc = ""
    count = 0
    for line in puzzle.readlines():
        line = line.strip()
        if len(line):
            acc += " " + line
        else:
            if is_valid(acc):
                count += 1
            acc = ""
    if acc and is_valid(acc):
        count += 1

    return count


if __name__ == "__main__":
    print(valid_passports("example.txt"))
    print(valid_passports("puzzle4.txt"))
