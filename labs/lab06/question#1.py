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

def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and False otherwise.
    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul=tree('roots',[tree('branch1',[tree('leaf'),tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    "*** YOUR CODE HERE ***"
    
    tree_queue=[t]
    while(len(tree_queue)> 0):
        current_tree  = tree_queue.pop(0)
        tree_name = label(current_tree)
        if tree_name == 'acorn':
            return True
        current_tree_branche = branches(current_tree)
        tree_queue.extend(current_tree_branche)

    return False    
