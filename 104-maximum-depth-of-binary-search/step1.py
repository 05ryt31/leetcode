# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root.val is null:
            return 0

        depth = 1

        def dfs(node: TreeNode, depth: int) -> int:
            if node.left is null and node.right is null:
                return
            else:
                depth += 1
                dfs(node.left) and dfs(node.right)
            return depth

        return dfs(root.val, 1)
