# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur, next = None, head, head
        while cur:
            next = cur.next
            cur.next, prev, cur = prev, cur, next
        return prev