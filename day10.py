import math
from itertools import cycle

def get_asteroids():
	asteroids = []
	input_file = 'day10input.txt'
	# input_file = 'day10sample_input.txt'
	with open(input_file, 'r') as f:
		for y, line in enumerate(f):
			for x, char in enumerate(line):
				# print(char, end='')
				if char == '#':
					asteroids.append((x, y))
	return asteroids


def rtheta(a, b):
	dx = b[0] - a[0]
	dy = a[1] - b[1] # reversed to flip y direction, same as -(b[1] - a[1])
	r = math.hypot(dx, dy)
	# theta = atan2(y, x) for cartesian angle
	# theta = atan2(x, y) for compass angle
	theta = math.degrees(math.atan2(dx, dy))
	
	# from [-180, 180) to [0, 360]
	if theta < 0: theta += 360

	return r, theta


def print_asteroids(asteroids, station=None):
	xmax = max(asteroids, key=lambda a: a[0])[0]
	ymax = max(asteroids, key=lambda a: a[1])[1]
	print('   ', end='')
	for x in range(xmax+1):
		print(x//10, end='')
	print('\n   ', end='')
	for x in range(xmax+1):
		print(x %10, end='')
	print()
	for y in range(ymax+1):
		print(f'{y:>2}', end=' ')
		for x in range(xmax+1):
			if (x, y) == station:
				print('█',end='')
			elif (x, y) in asteroids:
				print('#',end='')
			else:
				print('.',end='')
		print()
	print()


def print_line_of_sight(angles, cell_size=4):
	xmax = max(angles, key=lambda a: a[0])[0]
	ymax = max(angles, key=lambda a: a[1])[1]
	for y in range(ymax+1):
		for x in range(xmax+1):
			if (x, y) in angles:
				print(f'{len(angles[(x,y)]):>{cell_size}}',end='')
			else:
				print(' '*cell_size,end='')
		print()
	print()


def part1():
	angles = {a: set() for a in get_asteroids()}
	for a in angles:
		for b in angles:
			if a is not b:
				angles[a].add(rtheta(a, b)[1])
	best = max(angles, key=lambda a: len(angles[a]))
	return best, len(angles[best])


def part2(ordinal):
	laser = part1()[0]

	asteroids = [{'coord': asteroid,
				  'dist':  rtheta(laser, asteroid)[0],
				  'theta': rtheta(laser, asteroid)[1] 
				  } for asteroid in get_asteroids() if asteroid != laser]
	asteroids.sort(key=lambda asteroid:asteroid['dist'], reverse=True)

	# group by theta
	targets = {}
	for theta in set(a['theta'] for a in asteroids):
		targets[theta] = [a for a in asteroids if a['theta'] == theta]

	# cycle through repeatedly
	target_iter = cycle(sorted(targets))
	theta = next(target_iter)
	# only advance i after target pop, not every theta iter
	i = 0
	# while there are still asteroids in the target list
	while sum(map(lambda t: len(targets[t]), targets)):
		# iterate until we find an asteroid in the direction of theta
		while len(targets[theta]) == 0: theta = next(target_iter)
		# laser the closest asteroid! (pop because reverse in line 89)
		curr = targets[theta].pop()

		# print('{:>3}.  {:>6.2f}°  at  ({:>2}, {:>2})'.format(
		# 		i+1, theta, curr['coord'][0], curr['coord'][1]))
		
		if i == ordinal-1: return curr['coord']
		
		theta = next(target_iter)
		i += 1

	raise Exception(f'Could not find {ordinal}th asteroid')

print_asteroids(get_asteroids(), part1()[0])
print('Monitoring station @ {} will detect {} asteroids'.format(*part1()))
ast_num = 200
print(f'Laser\'s {ast_num}th target will be at {part2(ast_num)}')