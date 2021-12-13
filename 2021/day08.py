inp = open("input_day08.txt").read().splitlines()
segments = [x.split(" | ") for x in inp]

def part_1(segments):
	result = 0
	unique_signal_segments = [2, 3, 4, 7]
	for signal in segments:
		current_segments = signal[1].split()
		for segment in current_segments:
			if(len(segment) in unique_signal_segments):
				result += 1
	return result


def part_2(inp):
	result = 0
	for x,y in [x.split('|') for x in inp]: 
		l = {len(s): set(s) for s in x.split()}
		
		number = ""
		for z in y.split(" "):
			if len(z) == 2:
				number += "1"
			elif len(z) == 3:
				number += "7"
			elif len(z) == 4:
				number += "4"
			elif len(z) == 5:
				z = set(z)
				if l[3].issubset(z):
					number += "3"
				elif len(z.intersection(l[4])) == 3:
					number += "5"
				else:
					number += "2"
			elif len(z) == 6:
				z = set(z)
				if l[4].issubset(z):
					number += "9"
				elif l[3].issubset(z):
					number += "0"
				else:
					number += "6"
			elif len(z) == 7:
				number += "8"
		result += int(number)
	return result

print("Result Task One: {}".format(part_1(segments)))
print("Result Task Two: {}".format(part_2(inp)))