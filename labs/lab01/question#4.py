def sumNaturals(n):
    """ Sum all the first n natural numbers.
    >>> sumNaturals(3) # 1 + 2 + 3 = 6
    6
    >>> sumNaturals(5) # 1 + 2 + 3 + 4 + 5 = 15
    15
    """
    return n*(n+1)//2

