segments = open("input_day08.txt").read().splitlines()
segments = [x.split(" | ") for x in segments]

def part_1(segments):
	result = 0
	unique_signal_segments = [2, 3, 4, 7]
	for signal in segments:
		current_segments = signal[1].split()
		for segment in current_segments:
			if(len(segment) in unique_signal_segments):
				result += 1
	return result

print("Result Task One: {}".format(part_1(segments)))