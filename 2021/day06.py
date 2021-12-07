from collections import Counter, defaultdict

timer = open("input_day06.txt").read().split(',')
timer = [int(x) for x in timer]

counter = defaultdict(int, Counter(timer))

for _ in range(256):
	new_values = defaultdict(int)
	for key, value in counter.items():
		if key == 0:
			new_values[6] += value
			new_values[8] += value
		else:
			new_values[key-1] += value
	counter = new_values
result_task_two = sum(counter.values())
print("Result Task Two: {}".format(result_task_two))
