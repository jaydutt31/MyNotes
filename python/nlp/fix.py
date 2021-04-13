file = open("mylove.txt","w")

f = open("new.txt","r")

for x in f.readlines():
	th = x.lstrip()
	file.write(th)
	