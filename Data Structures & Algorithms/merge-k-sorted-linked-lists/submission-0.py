# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import inf
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = [head for head in lists] # [l0, l1, l2,...., lk]
        sentinel = ListNode(-1001)
        dummy = sentinel
        k = len(lists)

        # ith pointer has min val.   How to do this??? O(k) * 10**5
        for _ in range(k):
            while all(pointers):
                min_i = -1
                minval = inf
                for i, p in enumerate(pointers):
                    if minval > p.val:
                        min_i = i
                        minval = p.val

                sentinel.next = pointers[min_i]
                pointers[min_i] = pointers[min_i].next
                sentinel = sentinel.next
            
            for i, p in enumerate(pointers):
                if not p: 
                    del pointers[i]
                    break
        
        return dummy.next