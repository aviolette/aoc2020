from elves import striplines


def run_program(program):
    line_num = 0
    visited = set()
    acc = 0
    while line_num not in visited and line_num < len(program):
        instruction, value = program[line_num]
        visited.add(line_num)
        jump = 1
        if instruction == "acc":
            acc += int(value)
        elif instruction == "jmp":
            jump = int(value)
        line_num += jump
    return acc, line_num in visited


def get_program(file_name):
    return [line.split(" ") for line in striplines(file_name)]


def find_bad_boot_code(file_name):
    program = get_program(file_name)
    for line_num in range(0, len(program)):
        instruction, value = program[line_num]
        if instruction != "acc":
            program[line_num] = ["nop" if instruction == "jmp" else "jmp", value]
            acc, loops = run_program(program)
            if not loops:
                return acc
            program[line_num] = [instruction, value]


def find_acc_value(file_name):
    return run_program(get_program(file_name))[0]


if __name__ == "__main__":
    print(find_acc_value("example8a.txt"))
    print(find_acc_value("puzzle8.txt"))
    print(find_bad_boot_code("example8a.txt"))
    print(find_bad_boot_code("puzzle8.txt"))
