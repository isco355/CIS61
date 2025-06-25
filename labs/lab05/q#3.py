def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and
    the i-th element of s.
    >>> enumerate([6, 1, 'a'])
    [[0, 6], [1, 1], [2, 'a']]
    >>> enumerate('five', 5)
    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]
    """
    "*** YOUR CODE HERE ***"
    size= len(s)
    enumerate_list=[]
    index=0
    while(index < size):
        offset_index=index+start
        elem = s[index]
        temp_values = [offset_index,elem]
        enumerate_list.append(temp_values)
        index+=1
    return enumerate_list
