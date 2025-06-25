def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    min_value = min(a,b)
    max_value =max(a,b)
    remainder = max_value % min_value
    if remainder==0:
        return min_value

    return gcd(min_value,remainder)

    
