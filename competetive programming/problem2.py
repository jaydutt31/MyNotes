import timeit

def fib(n):
	if n<=2 :
		return 1
	else:
		return fib(n-1)+fib(n-2)

def dp_fib(n):
	fibb = {}
	for k in range(1,n+1):
		if k<=2:
			f=1
		else:
			f = fibb[k-1]+fibb[k-2]
		fibb[k] = f
	return fibb[n]

print(fib(500))


