# 動かないコード

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = head
        r = head[-1]

        while l, r and l != r:
            l = l.next
            r = r.next

            if l = r:
                return True
        return False