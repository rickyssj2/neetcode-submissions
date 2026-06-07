# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q. val:
            p, q = q, p

        while not (p.val <= root.val <= q.val):
            if q.val < root.val:
                root = root.left
            
            elif root.val < p.val:
                root = root.right
        
        return root