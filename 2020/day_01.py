"""Advent of Code 2020 Day 01 - Report Repair."""


def main():
    all_numbers = getNumbers()
    high_values, low_values = splitNumbers(all_numbers)
    answer_one = findTwoEntries(high_values, low_values)
    print("Two entries that add to 2020", answer_one)  # Task 1
    answer_two = findThreeEntries(all_numbers)
    print("Three entries that add to 2020", answer_two)  # Task 2


def getNumbers():
    all_numbers = []
    with open("input_day01.txt") as fp:
        for entry in fp.readlines():
            all_numbers.append(int(entry))
    return all_numbers


def splitNumbers(all_numbers):
    high_values = []
    low_values = []

    for entry in all_numbers:
        if entry > 1010:
            high_values.append(entry)
        else:
            low_values.append(entry)

    return (high_values, low_values)


def findTwoEntries(high_values, low_values):
    for high_value in high_values:
        for low_value in low_values:
            if high_value + low_value == 2020:
                answer_one = high_value * low_value
    return answer_one


def findThreeEntries(all_entries):
    for entry_1 in all_entries:
        for entry_2 in all_entries:
            for entry_3 in all_entries:
                if entry_1 == entry_2 or entry_2 == entry_3 or entry_1 == entry_3:
                    continue
                if entry_1 + entry_2 + entry_3 == 2020:
                    answer_two = entry_1 * entry_2 * entry_3
    return answer_two


if __name__ == "__main__":
    main()
