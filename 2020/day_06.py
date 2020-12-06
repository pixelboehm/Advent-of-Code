"""Advent of Code 2020 Day 6: Custom Customs"""

all_lines = []
all_groups = []
group = []

with open("input_day06.txt") as fp:
    for line in fp.readlines():
        all_lines.append(line)

all_lines = iter(all_lines)

while True:
    element = next(all_lines, False)
    if element != False:
        group.append(element.rstrip("\n"))
        if element == "\n":
            del group[-1]
            all_groups.append(group)
            group = []
    else:
        all_groups.append(group)
        break


def countAnswers(all_groups):
    overall_count = 0
    for group in all_groups:
        group_answers = ""
        for person in group:
            group_answers += person
        group_count = len(set(group_answers))
        overall_count += group_count
    return overall_count


overall_count = countAnswers(all_groups)
print(overall_count)  # answer one
