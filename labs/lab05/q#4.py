
import math
def squares(s):
    """Returns a new list containing square roots of the elements of the original list
    that are perfect squares.
    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    root_values = [  round(math.sqrt(number))  for number in s if  math.sqrt(number) %1 ==0]


    return root_values

