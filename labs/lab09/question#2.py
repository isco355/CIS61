#Constructor
def Tree(label, branches=[]):
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


def cumulative_sum(t): 
    """Mutates t so that each node's label becomes the sum of all labels in the corresponding subtree rooted at t. 
    >>> #below test case will not work. Don’t test it. 
    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)]) 
    >>> cumulative_sum(t) 
    >>> t Tree(16, [Tree(8, [Tree(5)]), Tree(7)]) 
    """ 
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return t
        
    branches_list = branches(t)
                
    sub_trees=[ cumulative_sum(sub_tree) for sub_tree in branches_list ]
    sub_tree_labels=[ label(sub_tree) for sub_tree in sub_trees ]

    
    cumulative_sub_tree_value = sum(sub_tree_labels)+label(t)
    new_tree = Tree(cumulative_sub_tree_value,sub_trees)

    return new_tree

