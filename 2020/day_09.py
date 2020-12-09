"""Advent of Code 2020 Day 9: Encoding Error"""

numbers = []

with open("input_day09.txt") as fp:
    for entry in fp.readlines():
        numbers.append(int(entry.rstrip("\n")))


def check(preamble, number):
    for item in preamble:
        for item2 in preamble:
            if item == item2:
                continue
            elif number == item + item2:
                return True
    return False


def findNumber(preamble_length):
    for i in range(preamble_length + 1, len(numbers)):
        preamble = numbers[i - preamble_length : i]
        ret = check(preamble, numbers[i])
        if ret == False:
            return numbers[i], i
    return None


def findSet(number, ranges):
    current = 0
    temp = []
    for last_start in range(0, ranges):
        index = last_start
        while current <= number:
            current += numbers[index]
            temp.append(numbers[index])
            if current == number:
                print(current)
                temp.sort()
                return temp[0], temp[-1]
            index += 1
        current = 0
        temp = []


first_result, index = findNumber(25)
print(first_result)  # answer_one
smallest_number, largest_number = findSet(first_result, index)
print(smallest_number + largest_number)  # answer_two
