import copy

with open("input_day11.txt") as f:
    seats = [list(line) for line in f.read().split()]

initial_seats = copy.deepcopy(seats)


def printSeats(seats_list):
    for row in seats_list:
        print(row)


occ_seats = 0


def checkNeighbors(y, x):
    counter = 0
    x_max = len(seats[0]) - 1
    y_max = len(seats) - 1

    if x > 0:
        if seats[y][x - 1] == "#":
            counter += 1
        # check left

    if x < x_max:
        if seats[y][x + 1] == "#":
            counter += 1
        # check right

    if y > 0:
        if seats[y - 1][x] == "#":
            counter += 1
        # check top

    if y < y_max:
        if seats[y + 1][x] == "#":
            counter += 1
        # check down

    if x > 0 and y > 0:
        if seats[y - 1][x - 1] == "#":
            counter += 1
        # check top left

    if x > 0 and y < y_max:
        if seats[y + 1][x - 1] == "#":
            counter += 1
        # check down left

    if x < x_max and y > 0:
        if seats[y - 1][x + 1] == "#":
            counter += 1
        # check top right

    if x < x_max and y < y_max:
        if seats[y + 1][x + 1] == "#":
            counter += 1
        # check down right

    return counter


def countOccupiedSeats(seats):
    counter = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                counter += 1
    return counter


temp_seats = copy.deepcopy(seats)
seats_changed = 1

while seats_changed != 0:
    seats_changed = 0
    for y in range(0, len(seats)):
        for x in range(0, len(seats[y])):

            if seats[y][x] == ".":
                continue

            occ_seats += checkNeighbors(y, x)

            if occ_seats == 0 and temp_seats[y][x] != "#":
                seats_changed += 1
                temp_seats[y][x] = "#"

            elif occ_seats >= 4 and temp_seats[y][x] != "L":
                seats_changed += 1
                temp_seats[y][x] = "L"

            occ_seats = 0
    seats = copy.deepcopy(temp_seats)
    # print("seats changed:", seats_changed)

print(countOccupiedSeats(seats))

seats = copy.deepcopy(initial_seats)


def visibleSeats(y, x):
    counter = 0
    x_max = len(seats[0])
    y_max = len(seats)

    if x > 0:
        for j in range(x - 1, -1, -1):
            if seats[y][j] == "#":
                counter += 1
                break
            elif seats[y][j] == "L":
                break
            # check left

    if x < x_max:
        for j in range(x + 1, x_max):
            if seats[y][j] == "#":
                counter += 1
                break
            elif seats[y][j] == "L":
                break
            # check right

    if y > 0:
        for j in range(y - 1, -1, -1):
            if seats[j][x] == "#":
                counter += 1
                break
            elif seats[j][x] == "L":
                break
            # check top

    if y < y_max:
        for j in range(y + 1, y_max):
            if seats[j][x] == "#":
                # print("down at index", j)
                counter += 1
                break
            elif seats[j][x] == "L":
                break
            # check down

    # fix diagonal funcions

    if x > 0 and y > 0:
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
            if seats[j][i] == "#":
                counter += 1
                break
            elif seats[j][i] == "L":
                break
            i -= 1
            j -= 1
        # check top left

    if x > 0 and y < y_max:
        i = x - 1
        j = y + 1
        while j <= y_max - 1 and i >= 0:
            if seats[j][i] == "#":
                counter += 1
                break
            elif seats[j][i] == "L":
                break
            j += 1
            i -= 1
        # check down left

    if x < x_max - 1 and y > 0:
        i = x + 1
        j = y - 1
        while j >= 0 and i <= x_max - 1:
            if seats[j][i] == "#":
                counter += 1
                break
            elif seats[j][i] == "L":
                break
            j -= 1
            i += 1
        # check top right

    if x < x_max - 1 and y < y_max - 1:
        i = x + 1
        j = y + 1
        while j <= y_max - 1 and i <= x_max - 1:
            if seats[j][i] == "#":
                counter += 1
                break
            elif seats[j][i] == "L":
                break
            j += 1
            i += 1
        # check down right

    return counter


temp_seats = copy.deepcopy(seats)
seats_changed = 1

while seats_changed != 0:
    seats_changed = 0
    for y in range(0, len(seats)):
        for x in range(0, len(seats[y])):
            if seats[y][x] == ".":
                continue

            occ_seats += visibleSeats(y, x)

            if occ_seats == 0 and temp_seats[y][x] != "#":
                seats_changed += 1
                temp_seats[y][x] = "#"

            elif occ_seats >= 5 and temp_seats[y][x] != "L":
                seats_changed += 1
                temp_seats[y][x] = "L"

            occ_seats = 0
    seats = copy.deepcopy(temp_seats)
    # print("seats changed:", seats_changed)

print(countOccupiedSeats(seats))
