waiting_time = -1
answer_one = 0

with open("input_day13.txt") as fp:
    timestamp = int(fp.readline().rstrip("\n"))
    busses = fp.readline().rstrip("\n").split(",")
    # busses[:] = [x for x in busses if x != "x"]


def getEarliestBus(waiting_time):
    for bus in busses:
        if bus == "x":
            continue
        value = int(bus)
        time = 0
        while time < timestamp:
            time += value

        if waiting_time == -1:
            waiting_time = time - timestamp

        elif time - timestamp < waiting_time:
            (waiting_time, quickest_bus) = time - timestamp, value
    return waiting_time, quickest_bus


waiting_time, quickest_bus = getEarliestBus(waiting_time)
answer_one = waiting_time * quickest_bus

print(answer_one)
