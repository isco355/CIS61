
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.
    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    
    current= 0
    previous = 0
   

    def nextStep():
        nonlocal current,previous
        if previous==0:
            previous=1
        else:
            next= current + previous
            previous=current
            current=next
        return current
    return nextStep
