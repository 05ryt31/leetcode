# step2 回答を見た後に自力で書いたコード

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        reverse_list = []
        curr = head

        while curr:
            reverse_list.append(curr)
            curr = curr.next

        new_head = reverse_list.pop()
        curr = new_head

        while reverse_list:
            curr.next = reverse_list.pop()
            curr = curr.next

        curr.next = None
        return new_head
        