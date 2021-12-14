heatmap = []
with open("input_day09.txt") as inp:
	for line in inp:
		heatmap.append(line.rstrip("\n"))

def part_1(heatmap):
	x_max = len(heatmap) - 1
	y_max = len(heatmap[1]) - 1
	low_points = []
	for x in range(len(heatmap)):
		for y in range(len(heatmap[1])):
			if x == 0 and y == 0:
				if heatmap[x+1][y] > heatmap[x][y] and heatmap[x][y+1] > heatmap[x][y]:
					low_points.append(heatmap[x][y])
			elif x == 0 and y == y_max:
				if heatmap[x+1][y] > heatmap[x][y] and heatmap[x][y-1] > heatmap[x][y]:
					low_points.append(heatmap[x][y])
			elif x == x_max and y == 0:
				if heatmap[x-1][y] > heatmap[x][y] and heatmap[x][y+1] > heatmap[x][y]:
					low_points.append(heatmap[x][y])
			elif x == x_max and y == y_max:
				if heatmap[x-1][y] > heatmap[x][y] and heatmap[x][y-1] > heatmap[x][y]:
					low_points.append(heatmap[x][y])
			elif x == 0:
				if heatmap[x+1][y] > heatmap[x][y] and heatmap[x][y+1] > heatmap[x][y] and heatmap[x][y-1] > heatmap[x][y]:
					low_points.append(heatmap[x][y])
			elif x == x_max:
				if heatmap[x-1][y] > heatmap[x][y] and heatmap[x][y+1] > heatmap[x][y] and heatmap[x][y-1] > heatmap[x][y]:
					low_points.append(heatmap[x][y])
			elif y == 0:
				if heatmap[x][y+1] > heatmap[x][y] and heatmap[x-1][y] > heatmap[x][y] and heatmap[x+1][y] > heatmap[x][y]:
					low_points.append(heatmap[x][y])
			elif y == y_max:
				if heatmap[x][y-1] > heatmap[x][y] and heatmap[x-1][y] > heatmap[x][y] and heatmap[x+1][y] > heatmap[x][y]:
					low_points.append(heatmap[x][y])
			else:
				if heatmap[x+1][y] > heatmap[x][y] and heatmap[x-1][y] > heatmap[x][y] and heatmap[x][y+1] > heatmap[x][y] and heatmap[x][y-1] > heatmap[x][y]:
					low_points.append(heatmap[x][y])
	result_list = sum([int(x)+1 for x in low_points])
	return result_list

print("Result Task One: {}".format(part_1(heatmap)))
