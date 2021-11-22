'''

Binary search :
    binary search is an algorithm that finds the position of a target value with a sorted array.

eg.
my_list = [2,3,4,5,7,8,9]

    seach for the element 7 in list.
    denote the element to be searched by K.

steps:
    1. sort the list
    2. compare 'k' with the middle most element in the list.
    3. if 'k' matches with the middle element then we return the mid index.
    4. else if 'k' is greater than middle element than the middle element then 'k' can lie only in right half of the list after the middle element so repeat the second and third step with the right half of the list.
    5. else if 'k' is smaller than the middle element repeat the second and third step with the left half of the list.

implemnetation:
    my_list = [2,3,4,5,7,8,9]
    
    middle element = 5
    as 7>5, ignore the left half

    now we have: [7,8,9]
    middle element = 8, and as 7<8, ignore the right half.

    finally we are left with 7 at the 4th index of the list.

Time Complexity:
    first iteration = n
    second iteration = n/2
    third iteration = n/4 = n/2 * 2
    .......
    last iteration = 1=n/2^y
    Here, y is the number of iteration performed 

    n = 2^y 
    log(n) = y
    time complexity = O(logn) 



'''