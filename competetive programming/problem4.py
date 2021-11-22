inp = [2,0,3,3,4,4,5]

freq = {}

for x in inp:
	if(x in freq):
		freq[x] += 1
	else:
		freq[x] = 1

print(list(freq.values()))