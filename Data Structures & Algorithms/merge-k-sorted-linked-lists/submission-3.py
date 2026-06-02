# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import inf
from heapq import heappush, heappop, heapify
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # pointers = [head for head in lists] # [l0, l1, l2,...., lk]
        sentinel = ListNode(-1001)
        dummy = sentinel
        k = len(lists)
        minheap = [(p.val, i, p) for i, p in enumerate(lists)] # [(1, l1), (1, l2), (3, l3)]
        heapify(minheap)
        # ith pointer has min val.   How to do this??? O(k) * 10**5
        
        while minheap:
            # print(minheap)
            _, i, p = heappop(minheap)

            sentinel.next = p
            p = p.next
            if p: heappush(minheap, (p.val,i ,p))
            sentinel = sentinel.next

        return dummy.next # nklogk