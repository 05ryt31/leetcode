# step1で書いたコード（動かないコード）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        middle = len(nums) // 2
        bst = TreeNode(nums[middle])
        # middleの両隣のindexをleft, rightとする
        left = middle - 1
        right = middle + 1

        while left > 0 or right < len(nums) - 1:
            if left < 0:
                break
            else:
                bst.left = nums[left]
                left -= 1

            if right > len(nums) - 1:
                break
            else:
                bst.right = nums[right]
                right += 1
        
        return bst
        