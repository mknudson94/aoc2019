from itertools import permutations, repeat

io = []

def intcode(p):
	ops = [3,8,1001,8,10,8,105,1,0,0,21,30,39,64,81,102,183,264,345,426,99999,3,9,1001,9,2,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1002,9,5,9,101,2,9,9,102,3,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]
	i = 0
	while i < len(ops):
		op = ops[i]

		if op%100 in [1,2,4,5,6,7,8]:
			param1 = ops[i+1] if op >= 100 and str(op)[-3] in '1' else ops[ops[i+1]]
		if op%100 in [1,2,5,6,7,8]:
			param2 = ops[i+2] if op >= 1000 and str(op)[-4] in '1' else ops[ops[i+2]]

		if op%100 == 1:
			ops[ops[i+3]] = param1 + param2
			i += 4
		elif op%100 == 2:
			ops[ops[i+3]] = param1 * param2
			i += 4
		elif op%100 == 3:
			param1 = ops[i+1]
			if p != None:
				ops[param1] = p
				p = None
			else:
				ops[param1] = io.pop()
			i += 2
		elif op%100 == 4:
			yield param1
			i += 2
		elif op%100 == 5:
			 i = param2 if param1 else i+3
		elif op%100 == 6:
			 i = param2 if not param1 else i+3
		elif op%100 == 7:
			ops[ops[i+3]] = 1 if param1 < param2 else 0
			i += 4
		elif op%100 == 8:
			ops[ops[i+3]] = 1 if param1 == param2 else 0
			i += 4
		elif op%100 == 99:
			return
		else:
			raise Exception(f'invalid operation: {ops[i]}')



def part1():

	global io

	max_found = 0
	best_setting = None
	for i, phase_settings in enumerate(permutations('01234')):

		io = [0]

		for p in map(int, phase_settings):
			io.append(next(intcode(p)))

		if io[0] > max_found:
			max_found = io[0]
			best_setting = phase_settings

	return max_found, phase_settings



def part2():

	global io
	max_found = 0
	best_setting = None
	for i, phase_settings in enumerate(permutations('56789')):

		io = [0]
		outputs = [0,0,0,0,0]

		amps = [intcode(int(p)) for p in phase_settings]

		try:
			while True:
				for i, amp in enumerate(amps):
					outputs[i] = next(amp)
					io.append(outputs[i])
		except StopIteration:
			max_local_found = outputs[4]
	
		if max_local_found > max_found:
			max_found = io[0]
			best_setting = phase_settings

	return max_found, phase_settings

				
print(part2())

# a(9,0) = 5
# b(8,5) = 9
# c(7,9) = 14
# d(6,14) = 31
# e(5,31) = 64
# a(None, 64)

# 37121 wrong
