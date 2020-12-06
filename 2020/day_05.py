input = "FBFBBFFRLR"
all_rows = []
all_seats = []
highest_seatID = 0

for i in range(0, 128):
    all_rows.append(i)

for i in range(0, 8):
    all_seats.append(i)


def getEntries():
    all_entries = []
    with open("input_day05.txt") as fp:
        for entry in fp.readlines():
            all_entries.append(entry)
    return all_entries


def getSeatID(input):
    rows = list(all_rows)
    seats = list(all_seats)

    for row_index in range(0, 7):
        current_half = len(rows) // 2

        if input[row_index] == "B":
            rows = rows[current_half:]
        else:
            rows = rows[:current_half]

    for seat_index in range(7, 10):
        current_half = len(seats) // 2

        if input[seat_index] == "R":
            seats = seats[current_half:]
        else:
            seats = seats[:current_half]

    current_seatID = rows[0] * 8 + seats[0]
    return current_seatID


all_entries = getEntries()

for entry in all_entries:
    current_seatID = getSeatID(entry)

    if current_seatID > highest_seatID:
        highest_seatID = current_seatID

print(highest_seatID)  # answer_one
