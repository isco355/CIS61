def fibonacciN(n):
    """Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is 
    the sum of the two preceding numbers
    >>> fibonacciN(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacciN(7) 
    13
    """
    iteration=0
    previous =0 
    current =1
    
    while(iteration < n-1):
        next = previous+current
        previous = current
        current= next
        iteration+=1
    return current
    
