def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n==1:
        return False
    divisor=2
    while(divisor < n):
        if(n % divisor ==0):
            return False
        divisor+=1
    return True



