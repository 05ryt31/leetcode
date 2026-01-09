# 動かないコード

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        
        return self.helper(root1, root2)

    def helper(self, node1: TreeNode, node2: TreeNode) -> TreeNode:
        while node1 is not None or node2 is not None:
            if node1 is None:
                node1.val = node2.val
            else:
                node1.val += node2.val
            self.helper(node1.left, node2.left)
            self.helper(node1.right, node2.right)
        return node1
        