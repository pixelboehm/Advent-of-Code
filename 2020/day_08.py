"""Advent of Code 2020 Day 8: Handheld Halting"""

instructions = []
acc = 0
visited = []


with open("input_day08.txt") as fp:
    for entry in fp.readlines():
        instructions.append(entry.rstrip("\n"))

index = 0
while index < len(instructions):
    current_entry = instructions[index]
    print(current_entry)
    if index in visited:
        break
    else:
        visited.append(index)

    if current_entry[:3] == "acc":
        value = int(current_entry[4:])
        acc += value

    if current_entry[:3] == "jmp":
        value = int(current_entry[4:]) - 1
        index += value

    if current_entry[:3] == "nop":
        index += 1
        continue

    index += 1

print(acc)  # answer one
