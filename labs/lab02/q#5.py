def sum_digits(n):
    """Sum all the digits of n.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    "*** YOUR CODE HERE ***"
    digits=n
    total =0
    while(digits >0):
        last_digit = digits%10
        total+=last_digit
        digits = (digits-last_digit)//10

    return total
