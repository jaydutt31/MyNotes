arr = [1,2,3,4,5,6,6]
n = len(arr)
count = 0


for x in range(0,n-1):
	for y in range(1,n):
		# y = 2
		# arr[y-1] = 1
		# arr[y] = 3

		if arr[y-1]<arr[y]:
			print(arr[y-1],arr[y])
			print(arr)
			arr[y-1],arr[y]=arr[y],arr[y-1]
			print("after",arr[y-1],arr[y])
			print(arr,"\n")

			# here, first element keeps shifting and comparing to the next value. so we use "y-1" to index the first element, and y as 
			# the element to compare. 

		# arr[y-1] = 2
		# arr[y] = 1
		
'''		
for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
'''

print(arr)




