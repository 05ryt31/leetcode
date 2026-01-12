# 動かないコード

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        hasTarget = False
        current_sum = 0
        self.checkPathSum(root, current_sum)

        def checkPathSum(self, node: Optional[TreeNode], current_sum: int):
            # leafまで辿り着いた時がnode is None、この時のcurrent_sumがtargetSumと一致しているかをチェック
            if node is None:
                hasTarget = (current_sum == targetSum)
            else:
                current_sum += int(node.val)
                self.checkPathSum(node.left, current_sum)
                self.checkPathSum(node.right, current_sum)

        return hasTarget
