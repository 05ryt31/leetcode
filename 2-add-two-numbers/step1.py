# 動かないコード

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0, l1)
        list1 = l1.val
        list2 = l2.val
        res = 0

        while list1 or list2:
            if res > 10:
                res = list1.val + list2.val + 1
            else:
                res = list1.val + list2.val
            if res >= 10:
                result.next = res % 10
            else: result.next = res
            list1 = list1.next
            list2 = list2.next
        return result.next