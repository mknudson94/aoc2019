count = 0
i0 = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0

def num():
	return int(''.join(map(str,[i5,i4,i3,i2,i1,i0])))

for i5 in range(2, 10):
	for i4 in range(i5, 10):
		for i3 in range(i4, 10):
			for i2 in range(i3, 10):
				for i1 in range(i2, 10):
					for i0 in range(i1, 10):
						if num() < 271973 or num() > 785961:
							continue
						if (   i5==i4            and i4!=i3
								or i4==i3 and i5!=i4 and i3!=i2
								or i3==i2 and i4!=i3 and i2!=i1
								or i2==i1 and i3!=i2 and i1!=i0
								or i1==i0 and i2!=i1            ):
							count += 1
print(count)

# 932 is wrong
