"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        sentinel = Node(-1)
        dummy = sentinel
        corresponding_node = {None: None}
        temp = head
        while head:
            new_node = Node(head.val)
            sentinel.next = new_node
            corresponding_node[head] = new_node
            sentinel = sentinel.next
            head = head.next

        # build randoms

        head = temp
        sentinel = dummy.next
        while head:
            sentinel.random = corresponding_node[head.random]
            sentinel = sentinel.next
            head = head.next

        return corresponding_node[temp]