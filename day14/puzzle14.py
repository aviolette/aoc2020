import re
from typing import List

from elves import striplines


def apply_value(rvalue, mask):
    rvalue = int(rvalue)
    new_val = rvalue
    for i, bit in enumerate(reversed(mask)):
        comp = pow(2, i)
        if bit == "0":
            new_val = new_val & ~comp
        elif bit == "1":
            new_val = new_val | comp
    return new_val


def combos_helper(address, mask, arr: List, index, result):
    for i in range(index, len(mask)):
        comp = pow(2, len(mask) - i - 1)
        if mask[i] == "0":
            value = "1" if bool(address & comp) else "0"
            result += value
        elif mask[i] == "1":
            result += "1"
        elif mask[i] == "X":
            combos_helper(address, mask, arr, i + 1, result + "0")
            combos_helper(address, mask, arr, i + 1, result + "1")
            return
    arr.append(result)


def combos(address, mask):
    results = []
    combos_helper(address, mask, results, 0, "")
    return results


def puzzle_two(file_name):
    mask = ""
    mem = {}
    for line in striplines(file_name):
        lvalue, rvalue = line.split(" = ")
        if lvalue == "mask":
            mask = rvalue
        else:
            m = re.search("(\d+)", lvalue)
            address = int(m.group(0))
            com = combos(address, mask)
            for target_address in com:
                mem[target_address] = int(rvalue)
    return sum([x for x in mem.values()])


def puzzle_one(file_name):
    mask = ""
    mem = {}
    for line in striplines(file_name):
        lvalue, rvalue = line.split(" = ")
        if lvalue == "mask":
            mask = rvalue
        else:
            m = re.search("(\d+)", lvalue)
            mem[f"{m.group(0)}"] = apply_value(rvalue, mask)
    return sum([x for x in mem.values()])


if __name__ == "__main__":
    #    print(puzzle_one("example14.txt"))
    #    print(puzzle_one("puzzle14.txt"))
    print(puzzle_two("example141.txt"))
    print(puzzle_two("puzzle14.txt"))
