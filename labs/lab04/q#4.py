def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def prime_recursive(n,divisor):
        if divisor == n:
            return True
        if (n%2==0):
            return False
        
        return prime_recursive(n,divisor+1)
    
    return prime_recursive(n,2)
        
    
