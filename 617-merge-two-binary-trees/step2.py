# 一部のテストケースで落ちてしまうコード

# Wrong Answer
# 128 / 182 testcases passed

# Input　
# root1 = [1,3,2,5]
# root2 = [2,1,3,null,4,null,7]
# Output
# [3,4,5,5]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        root1.val += root2.val
        self.mergeTrees(root1.left, root2.left)
        self.mergeTrees(root1.right, root2.right)
        return root1