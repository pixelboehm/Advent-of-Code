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
    answer_two = 0
    for group in all_groups:
        all_answers = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        group_answers = ""
        for person in group:
            group_answers += person
        group_answers = set(group_answers)
        group_count = len(group_answers)
        overall_count += group_count
        for person in group:
            person = [char for char in person]
            all_answers = [value for value in all_answers if value in person]
        answer_two += len(all_answers)

    return overall_count, answer_two


# result.intersection_update(s)

overall_count, answer_two = countAnswers(all_groups)
print(overall_count)  # answer one
print(answer_two)  # answer two
