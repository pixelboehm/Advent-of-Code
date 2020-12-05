"""Advent of Code 2020 Day 4: Passport Processing"""

all_lines = []
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]
answer_one = 0

with open("input_day04.txt") as fp:
    for line in fp.readlines():
        all_lines.append(line)


passport_dict = []
current_passport = dict()


def addKeyValuePair(dict, line, current_position):
    if current_position > 0:
        line = line[current_position + 1 :]
    else:
        line = line[current_position:]

    current_space = line.find(" ")

    if current_space == -1:
        key = line[: line.find(":")]
        value = line[line.find(":") + 1 :]
        value = value.rstrip("\n")
    else:
        key = line[: line.find(":")]
        value = line[line.find(":") + 1 : line.find(" ")]
        value = value.rstrip("\n")

    dict[key] = value

    if current_space != -1:
        return addKeyValuePair(dict, line, current_space)
    return dict


def checkPassport(passport):
    if all(item in passport.keys() for item in required_fields):
        return True


all_lines = iter(all_lines)

while True:
    element = next(all_lines, False)
    if element != False:
        current_passport = addKeyValuePair(current_passport, element, 0)
        if element == "\n":
            current_passport.popitem()
            passport_dict.append(current_passport)
            current_passport = {}
    else:
        passport_dict.append(current_passport)
        break


for passport in passport_dict:
    if checkPassport(passport) == True:
        answer_one += 1

print(answer_one)  # Task 1
