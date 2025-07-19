def naturals():
    i=1
    while(True):
        yield i
        i+=1
def scale(s, k): 
    """Yield elements of the iterable s scaled by a number k. 
    >>> s = scale([1, 5, 2], 5) 
    >>> type(s)
    <class 'generator'> 
    >>> list(s) 
    [5, 25, 10] 
    >>> m = scale(naturals(), 2) 
    >>> [next(m) for _ in range(5)] 
    [2, 4, 6, 8, 10] 
    """ 
    "*** YOUR CODE HERE ***"
    for value in s:
        yield value*k

