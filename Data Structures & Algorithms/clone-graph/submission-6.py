"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.cn = {None: None}
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        newNode = Node(node.val)
        self.cn[node.val] = newNode

        for nei in node.neighbors:
            if nei.val in self.cn:
                newNode.neighbors.append(self.cn[nei.val])
            else:
                newNode.neighbors.append(self.cloneGraph(nei))
        
        return newNode