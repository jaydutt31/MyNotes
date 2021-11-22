arr = [1,2,3,4,5,6,1,2,7,7,7]
n = len(arr)
count = 0
new = []
for x in range(0,n):
	key = arr[x]
	#x = 0
	#key = 1
	for y in range(0,n):
		#x = 4, y = 1, key = 5, arr[1] = 2
		#x = 4, y = 2, key = 5, arr[2] = 3
		#x = 4, y = 3, key = 5, arr[3] = 4
		#*x = 4, y = 4, key = 5, arr[4] = 5
		#x = 4, y = 5, key = 5, arr[5] = 6
		#x = 4, y = 6, key = 5, arr[6] = 1
		#x = 4, y = 7, key = 5, arr[7] = 2
		#x = 4, y = 8, key = 5, arr[8] = 3
		#x = 4, y = 9, key = 5, arr[9] = 4
		#x = 4, y = 10, key = 5, arr[10] = 5
		#x = 4, y = 11, key = 5, arr[11] = 6
	
		

		#x = 2, y = 1, key = 3, arr[1] = 2
		#*x = 2, y = 2, key = 3, arr[2] = 3
		#x = 2, y = 3, key = 3, arr[3] = 4
		#x = 2, y = 4, key = 3, arr[4] = 5
		#x = 2, y = 5, key = 3, arr[5] = 6
		#x = 2, y = 6, key = 3, arr[6] = 1
		#x = 2, y = 7, key = 3, arr[7] = 2*
		#x = 2, y = 8, key = 3, arr[8] = 3
		#x = 2, y = 9, key = 3, arr[9] = 4
		#x = 2, y = 10, key = 3, arr[10] = 5
		#x = 2, y = 11, key = 3, arr[11] = 6
		print(x,y,"old","\n")
		if x!=y and arr[y] == key:
			new.append(key)
			print(x,y,"new")
			count+=1
			print("found")
		

		
print(count)
print(new)