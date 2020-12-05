"""Advent of Code 2020 Day 4: Passport Processing"""

import re

all_lines = []
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]
answer_one = 0
answer_two = 0

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


def checkBirthYear(birth_year):
    return 1920 <= int(birth_year) <= 2002


def checkIssueYear(issue_year):
    return 2010 <= int(issue_year) <= 2020


def checkExpirationYear(exp_year):
    return 2020 <= int(exp_year) <= 2030


def checkHeight(height):
    unit = height[-2:]
    if unit != "cm" and unit != "in":
        return False
    value = int(height[:-2])

    if unit == "cm":
        return 150 <= value <= 193
    elif unit == "in":
        return 59 <= value <= 76


def checkHairColor(color):
    check = re.search(r"^#(?:[0-9a-f]{3}){1,2}$", color)
    if check != None:
        return True
    return False


def checkEyeColor(color):
    if color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False


def checkPassportID(value):
    # return len(identifier) == 9
    pid_regex = re.compile("[0-9]{9}")
    if pid_regex.match(value) and len(value) == 9:
        return True
    else:
        return False


def checkFields(passport, answer_one, answer_two):
    key_names = list(passport)
    if checkPassport(passport) == True:
        answer_one += 1
        current_check = False
        for entry in key_names:
            print(entry)
            if entry == "byr":
                current_check = checkBirthYear(passport[entry])

            elif entry == "iyr":
                current_check = checkIssueYear(passport[entry])

            elif entry == "eyr":
                current_check = checkExpirationYear(passport[entry])

            elif entry == "hgt":
                current_check = checkHeight(passport[entry])

            elif entry == "hcl":
                current_check = checkHairColor(passport[entry])

            elif entry == "ecl":
                current_check = checkEyeColor(passport[entry])

            elif entry == "pid":
                current_check = checkPassportID(passport[entry])

            elif entry == "cid":
                continue

            if current_check == False:
                return answer_one, answer_two
        answer_two += 1
        return answer_one, answer_two
    else:
        return answer_one, answer_two


for passport in passport_dict:
    answer_one, answer_two = checkFields(passport, answer_one, answer_two)


print(answer_one)
print(answer_two)
