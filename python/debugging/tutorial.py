'''
setting breakpoints
step forward line-by-line
show code as it executes
'''

import pdb

def transform(x, y):
	z = x + y

z = 5
x = 10
y = 15
n = 1000


pdb.set_trace()
transform(5, 10)
print("z = "+ str(z))
n = transform(2, 3)
print("n = "+ str(n))


