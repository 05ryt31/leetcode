# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        tail = result
        list1 = l1
        list2 = l2
        carry = 0

        while list1 or list2 or carry:
            x = list1.val if list1 else 0
            y = list2.val if list2 else 0
            
            total = x + y + carry
            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next
            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next
        return result.next