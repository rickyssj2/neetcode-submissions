"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cn = {None: None}

        def clone(node):
            if not node:
                return None
            
            newNode = Node(node.val)
            cn[node.val] = newNode

            for nei in node.neighbors:
                if nei.val in cn:
                    newNode.neighbors.append(cn[nei.val])
                else:
                    newNode.neighbors.append(clone(nei))
            
            return newNode

        return clone(node)