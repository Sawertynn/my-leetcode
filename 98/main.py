from treeNode import TreeNode, TreeBuilder
from solution import Solution

null = None

test_case_1 = [5, 4, 6, None, None, 3, 7]

# tnode = TreeBuilder(test_case_1)

head = TreeNode(5)
head.left = TreeNode(4)
head.right = TreeNode(6)
head.right.left = TreeNode(3)
head.right.right = TreeNode(7)

sol = Solution()
print(head)

result = sol.isValidBST(head)
print(result)

test_case_2 = [45,42,null,null,44,43,null,41]

head = TreeNode(45)
node = head
node.left = TreeNode(42)
node = node.left
node.right = TreeNode(44)
node = node.right
node.left = TreeNode(43)
node = node.left
node.left = TreeNode(41)

result = sol.isValidBST(head)
print(result)

head = TreeNode(1)
head.left = TreeNode(0)
head.right = TreeNode(0)

result = sol.isValidBST(head)
print(result)


