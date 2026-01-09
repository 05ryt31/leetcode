# 動かないコード

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        visited = []
        visited.append(head)

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            visited.append(slow)

            if slow == fast:
                if slow in visited:
                    return 

        return None