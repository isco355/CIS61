def couple(s1, s2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> s1 = [1, 2, 3]
    >>> s2 = [4, 5, 6]
    >>> couple(s1, s2)
    [[1, 4], [2, 5], [3, 6]]
    >>> s3 = ['c', 6]
    >>> s4 = ['s', '1']
    >>> couple(s3, s4)
    [['c', 's'], [6, '1']]
    """
    assert len(s1) == len(s2)
    "*** YOUR CODE HERE ***"
    size = len(s1)
    
    couple_list=[]
    i=0
    while (i <size):
        elem_a = s1[i]
        elem_b = s2[i]
        temp_couple=[elem_a,elem_b]
        couple_list.append(temp_couple)
        i+=1
    return couple_list



