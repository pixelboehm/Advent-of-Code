import math

position = open("input_day07.txt").read().split(',')
position = [int(x) for x in position]

position.sort()
mid = len(position) // 2
median = int((position[mid] + position[~mid]) / 2)

result_task_one = sum(map(lambda x: abs(x - median), position))
print("Result Task One: {}".format(result_task_one))

average = math.floor(sum(position) / len(position))

new_distances = list(map(lambda x: abs(x - average), position))

def calculate_fuel(number):
	return (number ** 2 + number) // 2

result_task_two = sum(map(calculate_fuel, new_distances))
print("Result Task Two: {}".format(result_task_two))