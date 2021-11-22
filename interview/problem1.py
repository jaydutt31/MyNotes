line = []

for x in range(1,100,3):
	line.append(x)

print(line)

miss = []

for x in range(1,101):
	if x in line:
		pass
	else:
		miss.append(x)

for x,y in zip(line,miss):
	print(x,y)

print(miss)


