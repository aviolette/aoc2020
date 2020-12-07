def splitlines(file_name):
    file = open(file_name, "r")
    for line in file.readlines():
        line = line.strip()
        yield line


def group_lines(file_name):
    group = []
    for line in splitlines(file_name):
        if len(line):
            group.append(line)
        else:
            yield group
            group = []
    if group:
        yield group
