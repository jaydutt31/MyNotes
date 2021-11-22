new =  {"a1":10,"b2":20,"c3":30}

keys = list(new.keys())
values = list(new.values())


for x in range(len(values)):
	values[x] += 1


final = dict(zip(keys,values))

print(final)


# output = {"a1":11,"b2":21,"c3":31} 
	
