from typing import Optional
from treeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result, _, _ = self.recursiveCheck(root)
        return result

    def recursiveCheck(self, root: Optional[TreeNode]) -> tuple:
        if root is None:
            return True, None, None

        left_isBST, left_min, left_max = self.recursiveCheck(root.left)
        if not left_isBST:
            return False, None, None
        if left_max is not None and left_max >= root.val:
            return False, None, None

        right_isBST, right_min, right_max = self.recursiveCheck(root.right)
        if not right_isBST:
            return False, None, None
        if right_min is not None and right_min <= root.val:
            return False, None, None

        values = [root.val, left_min, left_max, right_min, right_max]
        filtered = list(filter(lambda x: x is not None, values))

        if len(filtered) == 0:
            return True, None, None
        return True, min(filtered), max(filtered)
