import numpy as np

position = open("input_day07.txt").read().split(',')
position = [int(x) for x in position]

position.sort()
mid = len(position) // 2
res = int((position[mid] + position[~mid]) / 2)

result_task_one = sum(map(lambda x: abs(x-2), position))
