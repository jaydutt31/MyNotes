def norm_fib(n):
    if n<=2:
        return 1
    else:
        return norm_fib(n-1)+norm_fib(n-2)
    
def dp_fib(n):
    fib = {}
    for k in range(1,n+1):
        if k<=2: f= 1
        else: 
            f = fib[k-1]+fib[k-2]
        fib[k] = f
    return fib[n]

print(dp_fib(35))
