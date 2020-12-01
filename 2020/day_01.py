"""Advent of Code 2020 Day 01 - Report Repair."""

all_entries = []
high_values = []
low_values = []


with open("input_day01.txt") as fp:
    for entry in fp.readlines():
        all_entries.append(int(entry))

for entry in all_entries:
    if entry > 1010:
        high_values.append(entry)
    else:
        low_values.append(entry)

for high_value in high_values:
    for low_value in low_values:
        if high_value + low_value == 2020:
            answer_one = high_value * low_value

# Answer of first task
print("Two entries that add to 2020", answer_one)


for entry_1 in all_entries:
    for entry_2 in all_entries:
        for entry_3 in all_entries:
            if entry_1 == entry_2 or entry_2 == entry_3 or entry_1 == entry_3:
                continue
            if entry_1 + entry_2 + entry_3 == 2020:
                answer_two = entry_1 * entry_2 * entry_3

# Answer of first task
print("Three entries that add to 2020", answer_one)

