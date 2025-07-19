

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


def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    tree_name= label(t)
    if is_leaf(t):
        new_branch =[]   
        for val in vals:
            new_temp_tree = tree(val,[])
            new_branch.append(new_temp_tree)
        new_sub_tree = tree(tree_name,new_branch)
        return new_sub_tree
            
    branches_list = branches(t)
    for index,sub_tree in enumerate(branches_list):
        branches_list[index]=sprout_leaves(sub_tree,vals)

    new_tree = tree(tree_name,branches_list)
    return new_tree 




