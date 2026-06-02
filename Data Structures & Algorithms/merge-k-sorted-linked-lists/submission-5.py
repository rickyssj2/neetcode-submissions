# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import inf
from heapq import heappush, heappop, heapify
class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-1)
        dummy = sentinel

        while list1 and list2:
            if list1.val <= list2.val:
                sentinel.next = list1
                list1 = list1.next
            else:
                sentinel.next = list2
                list2 = list2.next
            sentinel = sentinel.next

        sentinel.next = list1 or list2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        interval = 1
        k = len(lists)
        if k == 0:
            return None
        while interval < k:
            for i in range(0, k - interval, 2 * interval):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval]) # O(n)
            interval *= 2
        return lists[0]

