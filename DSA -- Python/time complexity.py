'''
worst case time complexity is denoted by O (big o).

eg.
1.
if 5>3:
    print('true')
else:
    print('false')

this program executes only once, the operation performed here is constant
thatswhy, 
complexity = O(1)

2.
A = [2,3,4,9]
    task = to search 2 in the list
    sol: start with 0th index and iterate until 2 is found

This is the best case scenario

    task = to search 9 in the list
    sol: start with 0th index and iterate until 9 is found

This is worst case scenario

-------------------------------------------
number of | O(1) | O(n) | O(n^2) | O(n^3) |
records   |      |      |        |        |

    5       1ms    5ms     25ms     125ms
    6       1ms    6ms     36ms     216ms
    7       1ms    7ms     49ms     343ms
   
   5000     1ms   5000ms  25*10^6  125*10^0
                  =5 sec   =7 hrs   =4 yrs

-------------------------------------------


'''