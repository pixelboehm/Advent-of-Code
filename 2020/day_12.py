"""Advent of Code 2020 Day 12: Rain Risk"""

instructions = []
answer_one = 0
answer_two = 0

values = dict()
values["E"] = 0
values["W"] = 0
values["N"] = 0
values["S"] = 0

degrees = dict()
degrees["0"] = "N"
degrees["90"] = "E"
degrees["180"] = "S"
degrees["270"] = "W"


with open("input_day12.txt") as fp:
    for entry in fp.readlines():
        entry = entry.rstrip("\n")
        instruction = []
        instruction.append(entry[:1])
        instruction.append(entry[1:])
        instructions.append(instruction)


def turnLeft(current_heading, current_degree, degree):
    current_degree -= degree

    if current_degree < 0:
        current_degree = 360 - abs(current_degree)

    current_heading = degrees[str(current_degree)]

    return current_heading, current_degree


def turnRight(current_heading, current_degree, degree):
    current_degree += degree

    if current_degree >= 360:
        current_degree -= 360

    current_heading = degrees[str(current_degree)]

    return current_heading, current_degree


def taskOne():
    current_heading = "E"
    current_degree = 90

    for instruction in instructions:
        value_list = instruction[1:]
        value = list(map(int, value_list))[0]
        if instruction[0] == "F":
            values[current_heading] += value

        if instruction[0] == "E":
            values["E"] += value

        if instruction[0] == "W":
            values["W"] += value

        if instruction[0] == "N":
            values["N"] += value

        if instruction[0] == "S":
            values["S"] += value

        if instruction[0] == "L":
            current_heading, current_degree = turnLeft(
                current_heading, current_degree, value
            )

        if instruction[0] == "R":
            current_heading, current_degree = turnRight(
                current_heading, current_degree, value
            )

    answer_one = abs(values["E"] - values["W"]) + abs(values["N"] - values["S"])
    print(answer_one)


waypoint = (10, 1)
ship = (0, 0)


def changeLocation(ship, value):
    return (value * ship[0], value * ship[1])


def taskTwo():
    for instruction in instructions:
        print(instruction)
        value_list = instruction[1:]
        value = list(map(int, value_list))[0]
        if instruction[0] == "F":
            values = changeLocation(waypoint, value)
            ship = tuple(map(lambda i, j: i + j, ship, values))

        if instruction[0] == "E":
            waypoint = (waypoint[0] + value, waypoint[1])

        if instruction[0] == "W":
            waypoint = (waypoint[0] - value, waypoint[1])

        if instruction[0] == "N":
            waypoint = (waypoint[0], waypoint[1] + value)

        if instruction[0] == "S":
            waypoint = (waypoint[0], waypoint[1] - value)

        if instruction[0] == "L":
            temp = waypoint[0]

            if value == 90:
                waypoint = (-waypoint[1], temp)

            if value == 180:
                waypoint = (-waypoint[0], -waypoint[1])

            if value == 270:
                waypoint = (waypoint[1], -temp)

        if instruction[0] == "R":
            temp = waypoint[0]

            if value == 90:
                waypoint = (waypoint[1], -temp)
            if value == 180:
                waypoint = (-waypoint[0], -waypoint[1])
            if value == 270:
                waypoint = (-waypoint[1], temp)

    print(ship)
    answer_two = abs(ship[0]) + abs(ship[1])
    print(answer_two)

