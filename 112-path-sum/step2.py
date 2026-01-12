# step1を修正したVersion
# Time Complexity: O(n)
# Space Complexity: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        hasTarget = False

        def checkPathSum(node: Optional[TreeNode], current_sum: int):
            nonlocal hasTarget
            if node is None or hasTarget:
                return
            
            current_sum += node.val

            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    hasTarget = True
                return
            
            checkPathSum(node.left, current_sum)
            checkPathSum(node.right, current_sum)
        
        checkPathSum(root, 0)
        return hasTarget
