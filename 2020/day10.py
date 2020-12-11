"""Advent of Code 2020 10: Adapter Array"""

from collections import defaultdict

joltage = []
order = [
    0,
]
all_possibilities = []
ones = 0
threes = 1

with open("input_day10.txt") as fp:
    for entry in fp.readlines():
        joltage.append(int(entry.rstrip("\n")))
    joltage.sort()

current_joltage = 0

while True:
    found = False
    if current_joltage + 1 in joltage:
        current_joltage += 1
        order.append(current_joltage)
        ones += 1
        found = True

    elif current_joltage + 2 in joltage:
        current_joltage += 2
        order.append(current_joltage)
        found = True

    elif current_joltage + 3 in joltage:
        current_joltage += 3
        order.append(current_joltage)
        threes += 1
        found = True

    if not found:
        break
order.append(current_joltage + 3)
all_possibilities.append(order)

# this takes a lot of time
# for numbers in all_possibilities:
#     for i in range(1, len(numbers) - 1):
#         current = list(numbers)
#         if current[i + 1] - current[i - 1] <= 3:
#             current.remove(current[i])
#             if current not in all_possibilities:
#                 all_possibilities.append(current)
#             current = list(numbers)

paths = defaultdict(int)
paths[0] = 1

for adapter in order:
    for diff in range(1, 4):
        next_adapter = adapter + diff
        if next_adapter in order:
            paths[next_adapter] += paths[adapter]

last_key = list(paths)[-1]
print(paths[last_key])
