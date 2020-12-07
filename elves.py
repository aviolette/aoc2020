def striplines(file_name):
    file = open(file_name, "r")
    for line in file.readlines():
        line = line.strip()
        yield line


def stripsort(file_name, func):
    lines = [func(line) for line in striplines(file_name)]
    lines.sort()
    return lines


def group_lines(file_name):
    group = []
    for line in striplines(file_name):
        if len(line):
            group.append(line)
        else:
            yield group
            group = []
    if group:
        yield group
