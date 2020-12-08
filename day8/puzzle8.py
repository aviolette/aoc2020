from elves import striplines


def find_acc_value(file_name):
    program = [line.split(" ") for line in striplines(file_name)]
    line_num = 0
    visited = set()
    acc = 0
    while line_num not in visited or line_num > len(program):
        instruction, value = program[line_num]
        visited.add(line_num)
        jump = 1
        if instruction == "acc":
            acc += int(value)
        elif instruction == "jmp":
            jump = int(value)
        line_num += jump
    return acc


if __name__ == "__main__":
    print(find_acc_value("example8a.txt"))
    print(find_acc_value("puzzle8.txt"))
