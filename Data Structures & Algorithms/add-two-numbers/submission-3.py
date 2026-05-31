# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def makeInt(self, head):
        ptr = head
        s = ''
        while ptr:
            s += str(ptr.val)
            ptr = ptr.next
        return int(s[::-1])
    
    def makeLL(self, i):
        sentinel = ListNode(-1)
        dummy = sentinel

        if i == 0:
            return ListNode(0)

        while i:
            i, dig = divmod(i, 10)
            new_node = ListNode(dig)
            sentinel.next = new_node
            sentinel = sentinel.next

        return dummy.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.makeInt(l1)
        b = self.makeInt(l2)
        c = a + b

        return self.makeLL(c)