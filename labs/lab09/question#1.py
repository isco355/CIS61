class Link:
    """A linked list with a first element and the rest."""
    empty = ()  # Class attribute representing an empty list
    
    def __init__(self, first, rest=empty):
        # Verify that rest is either empty or another Link
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

def link_to_list(link): 

    """Takes a linked list and returns a Python list with the same elements. 
    >>> link = Link(1, Link(2, Link(3, Link(4)))) 
    >>> link_to_list(link) [1, 2, 3, 4] 
    >>> link_to_list(Link.empty) [] 
    """ 
    "*** YOUR CODE HERE ***"
    while(link is not Link.empty):
        label = link.first
        values.append(label)
        link=link.rest
    return values
