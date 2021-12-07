timer = open("input_day06.txt").read().split(',')
timer = [int(x) for x in timer]

def decrease_timer(timer):
	timer = [x - 1 for x in timer]
	return timer

def reset_timer(timer):
	for i in range(len(timer)):
		if timer[i] == -1:
			timer[i] = 6
			timer.append(8)
	return timer

for i in range(0, 80):
	timer = decrease_timer(timer)
	timer = reset_timer(timer)
	
print(len(timer))
