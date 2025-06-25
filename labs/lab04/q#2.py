def hailstone(n):
    """ Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n==1:
        return 1
    is_even = (n%2==0)
    new_value = n//2 if is_even  else (n*3)+1
    return 1+hailstone(new_value)
    
