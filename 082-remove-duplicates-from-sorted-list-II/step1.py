# 動きはするが間違っているコード

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = prev.next

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr = curr.next.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return head
