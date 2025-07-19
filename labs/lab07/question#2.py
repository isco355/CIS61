def group_by(seq, fn): 
    """ 
    >>> group_by([12, 23, 14, 45], lambda p: p // 10) 
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(list(range(-3, 4)), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]} 
    """
    groups={}
    for n in sorted(seq):
        key = fn(n)
        if key in groups:
            groups[key].append(n)
        else:
            groups[key]=[n]
    sorted_group=dict(sorted(groups.items(),key=lambda items: items[0]) )
    return sorted_group
