

# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selectors


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


def height(t):
    """Return the height of a tree. 
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)]) 
    >>> height(t) 
    2 
    """
    def calculateHeight(root, level):
        if is_leaf(root):
            return level

        branches_list = branches(root)
        sub_trees_height = [calculateHeight(
            sub_tree, level+1) for sub_tree in branches_list]

        max_height = max(sub_trees_height)
        return max_height

    tree_height = calculateHeight(t, 0)
    return tree_height
