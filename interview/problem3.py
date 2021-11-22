roll = "5"
# result = "46359"
#roll = "14"

result=[]
#roll = list(roll)

#result = new = [roll[i:i + 2] for i in range(0, len(roll), 2)]

for i in range(0,len(roll),2):
	new = roll[i:i+2]
	result.append(new)

print(result)
new_roll = ""
for i in range(len(result)):
	x = result[i]
	a = int(x[0])
	try:
		b = int(x[1])
	except:
		a = str(a)
		new_roll+=a
		break
	if a>b:
		a = str(a)
		new_roll+=a 

	elif b>=a:
		b = str(b)
		new_roll+=b



print(new_roll)



#print(roll)






