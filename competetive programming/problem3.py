inp = "I!am!a!coder" 

rev = inp.split("!")
print(rev)

ans = ""

for i in range(1,len(rev)+1):
	ans += rev[-i]+"!"
	

	

print(ans)
