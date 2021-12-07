vents = open("input_day05.txt").read().splitlines()
visited = {}


def calculate_overlaps(use_diagonals = False):
	for line in vents:
		l, r = line.split(' -> ')
		x1, y1 = map(int, l.split(','))
		x2, y2 = map(int, r.split(','))

		if x1 == x2:
			if y1 >= y2:
				min_y = y2
				max_y = y1
			else:
				min_y = y1
				max_y = y2

			for y in range(min_y, max_y+1):
				if (x1, y) not in visited:
					visited[(x1, y)] = 1
				else:
					visited[(x1, y)] += 1

		elif y1 == y2:
			if x1 >= x2:
				min_x = x2
				max_x = x1
			else:
				min_x = x1
				max_x = x2
			
			for x in range(min_x, max_x+1):
				if (x, y1) not in visited:
					visited[(x, y1)] = 1
				else:
					visited[(x, y1)] += 1

		else:
			if use_diagonals == True:
				distance_x = x2 - x1
				distance_y = y2 - y1

				if (x1, y1) not in visited:
					visited[(x1, y1)] = 1
				else:
					visited[(x1, y1)] += 1


				while x1 != x2:
					x1 = x1 + (distance_x // abs(distance_x))
					y1 = y1 + (distance_y // abs(distance_y))

					if (x1, y1) not in visited:
						visited[(x1, y1)] = 1
					else:
						visited[(x1, y1)] += 1

calculate_overlaps(False)
result_task_one = len([key for key, value in visited.items() if value >= 2])
print("Result Task One: {}".format(result_task_one))

