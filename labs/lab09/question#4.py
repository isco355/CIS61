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

def bstMinValue(t):
    m = label(t)
    for b in branches(t):
        m = min(m, bstMinValue(b))
    return m

def bstMaxValue(t):
    m = label(t)
    for b in branches(t):
        m = max(m, bstMaxValue(b))
    return m
     
def validLeft(t,node):
    left =(bstMaxValue(node) <= label(t)) and is_bst(node)

    return left
def validRight(t,node):
    right=(bstMinValue(node) > label(t)) and is_bst(node)
    return right

def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.
    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """

    bs = branches(t)
    if len(bs) > 2:
        return False

    if len(bs) == 1:
        node = bs[0]
        left_valid = validLeft(t,node)
        right_valid =validRight(t,node)
        return left_valid or right_valid

    if len(bs) == 2:
        left, right = bs
        left_valid = validLeft(t,left)
        right_valid =validRight(t,right)

        return left_valid and right_valid
    return True


