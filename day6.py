input_file = 'day6input.txt'
# input_file = 'day6sample_input.txt'
# input_file = 'day6sample_input2.txt'

orbits = {}

with open(input_file, 'r') as f:
	for line in f:
		line = line.strip('\n\r')
		a, b = line.split(')')
		orbits[b] = a

def longest_path(planet):
	count = 0
	# print(planet, end='')
	while planet := orbits.get(planet):
		# print('=>', planet, end='', sep='')
		count += 1
	# print()
	return count

def part1():
	total = 0
	for planet in orbits:
		# print('*', planet, '*', sep='')
		total += longest_path(planet)
	return total

def part2():
	santas_orbits = set()
	planet = orbits['SAN']
	while planet := orbits.get(planet):
		santas_orbits.add(planet)

	common_planet = orbits['YOU']
	path_len = 0
	while common_planet not in santas_orbits:
		common_planet = orbits[common_planet]
		path_len += 1
	
	santas_planet = orbits['SAN']
	while santas_planet != common_planet:
		santas_planet = orbits[santas_planet]
		path_len += 1

	return path_len


print(part2())
