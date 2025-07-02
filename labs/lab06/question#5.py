


#Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

#Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    if t==None:
        return
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def double_tree(t): 
    """Return a tree with the square of every element in t 
    >>> numbers = tree(1,[tree(2,[tree(3),tree(4)]),tree(5,[tree(6,[tree(7)]),tree(8)])]) 
    >>> print_tree(double_tree(numbers)) 
    2
      4
        6 
        8 
      10 
        12 
          14 
        16 
    """
    branches_list = branches(t)
                
    sub_trees=[ double_tree(sub_tree) for sub_tree in branches_list ]

    label_name = label(t)

    double_value = label_name*2

    new_tree = tree(double_value,sub_trees)

    return new_tree


