numbers, *boards = open('input_day04.txt').read().split('\n\n')
numbers = [int(n) for n in numbers.split(',')]
boards = [line.split('\n') for line in boards]
boards = [[list(filter(None, line.split(' '))) for line in board] for board in boards]
boards = [[[[int(nr), False] for nr in line] for line in board if line != []] for board in boards]
finished_boards = []

def mark_number(num):
	for board in boards:
		for line in board:
			for number in line:
				if number[0] == num:
					number[1] = True


def check_row(line):
	for number in line:
		if number[1] == False:
			return False
	return True

def check_column(board):
	for column in range(len(board)):
		for col_number, col in enumerate(board):
			if col[column][1] == False:
				break
			elif col_number == 4:
				return True
	return False

def play_bingo():
	counter = 0
	first_result = None
	last_result = 0
	for number in numbers:
		counter+=1
		mark_number(number)
		for board in boards:
			for line in board:
				if check_row(line) == True and board not in finished_boards:
					last_result = calculate_result(board, number)
					if first_result == None:
						first_result = last_result
					finished_boards.append(board)
			if check_column(board) == True and board not in finished_boards:
				last_result = calculate_result(board, number)
				if first_result == None:
					first_result = last_result
				finished_boards.append(board)
	return first_result, last_result

def calculate_result(board, number):
	unmarked = 0
	for line in board:
		for num in line:
			if num[1] == False:
				unmarked += num[0]
	return unmarked * number

result_task_one, result_task_two = play_bingo()	
print("Result Task One: {}".format(result_task_one))
print("Result Task Two: {}".format(result_task_two))

