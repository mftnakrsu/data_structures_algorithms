#normal
def fib(n):
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number

#recursion
def fib_recursion(n):
    #base condition
    if n==0 or n==1:
        return n
    
    # rec condition
    return fib(n-1)+fib(n-2) 
    

if __name__=='__main__':
    print(fib_recursion(5))
    print(fib(5))