all_bags = []
bag_counter = 0


def findNumber(string):
    for index in range(0, len(string)):
        if string[index].isdigit():
            return index
    return -1


def search(color):
    for bags in all_bags:
        if color in bags[1:]:
            colors.add(bags[0])
            search(bags[0])


with open("input_day07.txt") as fp:
    current_bag = []
    for entry in fp.readlines():
        current_bag.append(entry[: entry.find("contain") - 2].rstrip("s"))
        entry = entry[entry.find("contain") :]
        next_number = findNumber(entry)

        if next_number == -1:
            all_bags.append(current_bag)
            current_bag = []
            continue

        while True:
            if entry.find(",") < entry.find(".") and entry.find(",") > 0:
                current_bag.append(entry[next_number + 2 : entry.find(",")].rstrip("s"))
                entry = entry[entry.find(",") + 1 :]
                next_number = findNumber(entry)
            else:
                next_number = findNumber(entry)
                current_bag.append(entry[next_number + 2 : entry.find(".")].rstrip("s"))
                break

        all_bags.append(current_bag)
        current_bag = []

colors = set()

if __name__ == "__main__":
    search("shiny gold bag")
    print(len(colors))
