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
            next, cur.next, prev = cur.next, prev, cur
            cur = next
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = prev_tail = ListNode(-1)
        l = r = head

        # Reverse in k groups
        while True:
            t = k - 1
            while r and t:
                r, t = r.next, t - 1
            if not r: break
            tmp, r.next = r.next, None
            r = tmp
            prev_tail.next = self.reverseList(l)
            prev_tail, l = l, r

        prev_tail.next = l
        return sentinel.next
