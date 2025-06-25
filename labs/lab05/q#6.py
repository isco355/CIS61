def flatten(lst):
    """Returns a flattened version of lst.
    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    new_list=[]
    for elem in lst:
        if type(elem)==list:
            new_list.extend(flatten(elem))
        else:
            new_list.append(elem)

    return new_list 
        
