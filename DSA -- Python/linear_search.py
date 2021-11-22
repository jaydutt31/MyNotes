'''

1. linear search or sequential search is a mehtod fro finding an element within a list
2. it sequentially checks each element of the list until a match is found or the whole list has been seached.

eg.
my_list = [2,3,4,5,7,8,9]

step 1: start with the leftmost element of the list and compare one by one
step 2: if the key element is found return the index of the element and break the loop.
step 3: if the key element is not found in the list return -1

sol: 
    for i in range(len(my_list)):
        if my_list==8:
            print(i)
        else:
            print("elemnt not found")

worst case scenario:
    Number of operations = lenght of the list
    time complexity of linear searh = O(n)

'''



