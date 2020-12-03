"""Advent of Code 2020 Day 3: Toboggan Trajectory"""

tree = []


def checkForTree(char):
    return char == "#"


with open("input_day03.txt") as fp:
    for entry in fp.readlines():
        entry = entry.rstrip("\n")
        tree.append(entry)

x = 3
length = len(tree[0])
tree_counter = 0

for y in range(1, len(tree)):
    if x >= length:
        x = x - length
    if checkForTree(tree[y][x]):
        tree_counter += 1
    x += 3

print(tree_counter)  # Task 1

