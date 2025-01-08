from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __getitem__(self, key):
        if key == 0:
            return self.left
        if key == 1:
            return self.right
        raise IndexError

    def __setitem__(self, key, value):
        if key == 0:
            self.left = value
        elif key == 1:
            self.right = value
        else:
            raise IndexError


def TreeBuilder(values: list[Optional[int]]) -> Optional[TreeNode]:
    if len(values) == 0:
        return None

    head = TreeNode(values[0])
    node = head

    # numbering starts with 1 - it is important
    for i, val in enumerate(values[1:], 2):
        pos = i
        
        while pos > 0b11:
            node[0]

    return head



