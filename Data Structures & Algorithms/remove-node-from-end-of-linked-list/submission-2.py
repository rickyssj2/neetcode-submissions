# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(n) - single pass
        dummy = ListNode(-1)
        dummy.next = head

        prev, R = dummy, head

        # Boost R
        for _ in range(k):
            R = R.next
        
        while R:
            R = R.next
            prev = prev.next
        
        prev.next = prev.next.next

        return dummy.next
        
