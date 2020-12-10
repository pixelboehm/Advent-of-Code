joltage = []
switches = []
ones = 0
threes = 1

with open("input_day10.txt") as fp:
    for entry in fp.readlines():
        joltage.append(int(entry.rstrip("\n")))
    joltage.sort()

current_joltage = 0

while True:
    found = False
    if current_joltage + 1 in joltage:
        current_joltage += 1
        ones += 1
        print("one:", current_joltage)
        found = True

    elif current_joltage + 2 in joltage:
        current_joltage += 2
        print("two")
        found = True

    elif current_joltage + 3 in joltage:
        current_joltage += 3
        threes += 1
        print("three:", current_joltage)
        found = True

    if not found:
        break

print(ones * threes)

