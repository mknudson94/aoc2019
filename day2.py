
def p(arr):
	for i in range(len(arr)):
		print(arr[i], end=', ')
		if i % 4 == 3 or arr[i] == 99:
			print()
	print()

def part1(noun, verb):
	ops = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,9,23,1,23,9,27,1,10,27,31,1,13,31,35,1,35,10,39,2,39,9,43,1,43,13,47,1,5,47,51,1,6,51,55,1,13,55,59,1,59,6,63,1,63,10,67,2,67,6,71,1,71,5,75,2,75,10,79,1,79,6,83,1,83,5,87,1,87,6,91,1,91,13,95,1,95,6,99,2,99,10,103,1,103,6,107,2,6,107,111,1,13,111,115,2,115,10,119,1,119,5,123,2,10,123,127,2,127,9,131,1,5,131,135,2,10,135,139,2,139,9,143,1,143,2,147,1,5,147,0,99,2,0,14,0]
	ops[1] = noun
	ops[2] = verb
	i = 0
	while i < len(ops):
		try:
			if ops[i] == 1:
				ops[ops[i+3]] = ops[ops[i+1]] + ops[ops[i+2]]
			elif ops[i] == 2:
				ops[ops[i+3]] = ops[ops[i+1]] * ops[ops[i+2]]
			elif ops[i] == 99:
				break
		except:
			pass
		finally:
			i += 4
	return ops[0]
# wrong: 2880733
print(part1(12, 2))

def part2():
	noun = 0
	verb = 0
	for noun in range(200):
		for verb in range(200):
			if part1(noun, verb) == 19690720:
				return noun, verb

print(part2())
