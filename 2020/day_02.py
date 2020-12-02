"""Advent of Code 2020 Day 2: Password Philosophy."""

from collections import Counter


def prepareDictionary(items, string):
    key = string[: string.find(":")]
    value = string[string.find(":") + 2 :]
    items.setdefault(key, []).append(value)
    return items


def getCharacter(string):
    return string[-1]


def getNumberRange(string):
    lower_number = int(string[: string.find("-")])
    higher_number = int(string[string.find("-") + 1 : string.find(" ")])
    return lower_number, higher_number


def getNumberOfCharacters(string, char):
    count = Counter(string)
    amount = count[char]
    return amount


def main():
    items = dict()
    answer_one = 0
    with open("input_day02.txt") as fp:
        for entry in fp.readlines():
            items = prepareDictionary(items, entry)

    for key, value_list in items.items():
        char = getCharacter(key)
        for value in value_list:
            lower_number, higher_number = getNumberRange(key)
            actual_number = getNumberOfCharacters(value, char)

            if lower_number <= actual_number <= higher_number:
                result += 1
    print(answer_one)  # Task 1


if __name__ == "__main__":
    main()

