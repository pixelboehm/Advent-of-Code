"""Advent of Code 2020 Day 4: Passport Processing"""

all_lines = []
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]
answer_one = 0

with open("input_day04.txt") as fp:
    for line in fp.readlines():
        all_lines.append(line)

current_passport = []
passports = []

all_lines = iter(all_lines)

while True:
    element = next(all_lines, False)
    if element != False:
        current_passport.append(element)
        if element == "\n":
            del current_passport[-1]
            passports.append(current_passport)
            current_passport = []
    else:
        passports.append(current_passport)
        break


def findColons(string):
    return [i for i, char in enumerate(string) if char == ":"]


def checkPassport(passport):
    current_fields = []
    for entry in passport:
        colon_list = findColons(entry)
        for index in colon_list:
            current_fields.append(entry[index - 3 : index])

    if all(item in current_fields for item in required_fields):
        return 1
    return 0


for passport in passports:
    answer_one += checkPassport(passport)

print(answer_one)  # Task 1

