# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if not node:
                return (True, 0)
            
            lbal, ldpt = solve(node.left)
            rbal, rdpt = solve(node.right)
            curdpt = 1 + max(ldpt, rdpt)

            if not lbal or not rbal:
                return (False, curdpt)
            
            curbal = abs(ldpt - rdpt) <= 1

            return (curbal, curdpt)
        
        return solve(root)[0]

