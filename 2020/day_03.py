"""Advent of Code 2020 Day 3: Toboggan Trajectory"""

tree = []


def checkForTree(char):
    return char == "#"


with open("input_day03.txt") as fp:
    for entry in fp.readlines():
        entry = entry.rstrip("\n")
        tree.append(entry)


def checkSlopes(step_x, step_y):
    x = step_x
    y = step_y
    tree_counter = 0
    length_x = len(tree[0])
    while y < len(tree):
        if x >= length_x:
            x = x - length_x
        if checkForTree(tree[y][x]):
            tree_counter += 1
        x += step_x
        y += step_y
    return tree_counter


tree_counter = checkSlopes(3, 1)
print(tree_counter)  # Task 1


step_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
answer_two = 1

for step in step_list:
    value = checkSlopes(step[0], step[1])
    answer_two = answer_two * value

print(answer_two)  # Task 2

