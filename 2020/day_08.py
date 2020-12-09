"""Advent of Code 2020 Day 8: Handheld Halting"""

instructions = []


with open("input_day08.txt") as fp:
    for entry in fp.readlines():
        instructions.append(entry.rstrip("\n"))


def execute(instructions):
    index = 0
    acc = 0
    visited = []
    while index < len(instructions):
        terminated = False
        current_entry = instructions[index]
        visited.append(index)

        if current_entry[:3] == "acc":
            value = int(current_entry[4:])
            acc += value
            index += 1

        if current_entry[:3] == "jmp":
            value = int(current_entry[4:])
            index += value

        if current_entry[:3] == "nop":
            index += 1
            continue

        if index in visited:
            break
        else:
            terminated = True
    return terminated, acc


def switchInstruction():
    for last_index in range(0, len(instructions)):
        local_instructions = [i for i in instructions]
        if local_instructions[last_index][:3] == "jmp":
            local_instructions[last_index] = "nop" + local_instructions[last_index][4:]
            last_index += 1
        elif local_instructions[last_index][:3] == "nop":
            local_instructions[last_index] = "jmp" + local_instructions[last_index][4:]
            last_index += 1
        else:
            last_index += 1
            continue

        result, value = execute(local_instructions)
        if result == True:
            break
    return value


print(execute(instructions))  # answer one
print(switchInstruction())  # answer two

