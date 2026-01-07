# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        prev = head
        curr = prev.next

        while curr:
            if prev == curr:
                prev.next = None
                prev = curr
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head