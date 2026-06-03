# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> List[Optional[ListNode]]:
        # Ratta mar
        prev, cur, next = None, head, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(-1)
        dummy = sentinel

        prev_tail = sentinel
        l = r = head

        # Reverse in k groups
        while True:
            t = k - 1
            while r and t:
                r = r.next
                t -= 1
            if not r: break

            tmp = r.next
            r.next = None
            r = tmp
            new_head, new_tail = self.reverseList(l)

            prev_tail.next = new_head
            prev_tail = new_tail
            l = r

        
        prev_tail.next = l
        return dummy.next
