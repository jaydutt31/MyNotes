'''

bubble sort is a simple sorting algorithm that repeatidly iterates through the list, compares adjacent elements and swaps them if they are in the wrong order, and this process is repeated until the list is sorted.

my_list = [3,1,4,7,2]

First Pass:
    [3,1,4,7,2] -> [1,3,4,7,2] Since 1 is less than 3, 1 and 3 are swapped.
    [1,3,4,7,2] -> [1,3,4,7,2] Since, 3 and 4 are already in order so , algorithm does not swap them.
    [1,3,4,7,2] -> [1,3,4,7,2] Since, 4 and 7 are already in order so , algorithm does not swap them.
    [1,3,4,7,2] -> [1,3,4,2,7] Since 2 is less than 7, 7 and 2 are swapped.

Second Pass:
    [1,3,4,7,2] -> [1,3,4,2,7] Do not swap since 1 and 3 are already in order.
    [1,3,4,7,2] -> [1,3,4,2,7] Do not swap since 3 and 4 are already in order.
    [1,3,4,7,2] -> [1,3,2,4,7] swap since 2 is less than 4.

Third Pass:
    [1,3,2,4,7] -> [1,3,2,4,7] Do not swap since 1 and 3 are in order.
    [1,3,2,4,7] -> [1,2,3,4,7] swap since 2 is less than 3.

Fourth Pass:
    [1,2,3,4,7] -> [1,2,3,4,7] No change.


Time Complexity :
    i = 1            n times
    i = 2            n-1 times
    i = 3            n-2 times
    ....             .....
    i = n            1 times

    Total number of operations = n+(n-1)+(n-2)+(n-3)+(n-4)...
    n number os n's = n*n+(1+2+3+...)
    Time Complexity = O(n^2)
    
'''