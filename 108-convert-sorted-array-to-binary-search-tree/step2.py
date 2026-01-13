# step1の書き方に一番近い、正解のコード
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        middle = len(nums) // 2
        bst = TreeNode(nums[middle])
        
        left_nums = nums[:middle]
        right_nums = nums[middle + 1:]

        bst.left = self.sortedArrayToBST(left_nums)
        bst.right = self.sortedArrayToBST(right_nums)
        
        return bst
