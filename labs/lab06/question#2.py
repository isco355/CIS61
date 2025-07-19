
#Constructor
def tree(label, branches=[]):
    # for branch in branches:
        # assert is_tree(branch)
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

def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label that appears 
    in vals removed.  Return None if the entire tree is pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"
    tree_name= label(t)
    if is_leaf(t) and (tree_name in vals):
            return None
            
    branches_list = branches(t)
    for index,sub_tree in enumerate(branches_list):
        new_sub = prune_leaves(sub_tree,vals)
        branches_list[index]=new_sub

    new_tree = tree(tree_name,branches_list)
    return new_tree 



