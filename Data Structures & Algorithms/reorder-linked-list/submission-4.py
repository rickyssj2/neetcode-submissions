# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Ratta mar
        prev, cur, next = None, head, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        sentinel = ListNode(-1)
        dummy = sentinel
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow = midpoint
        r = self.reverseList(slow)
        l = head

        while r and l != r:
            sentinel.next = l
            l = l.next
            sentinel = sentinel.next
            sentinel.next = r
            r = r.next
            sentinel = sentinel.next
        

        head = dummy.next


        