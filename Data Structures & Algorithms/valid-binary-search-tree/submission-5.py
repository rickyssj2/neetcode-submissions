# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root):
            if not root:
                return True, 1001, -1001
            
            lvalid, lmin, lmax = solve(root.left)
            rvalid, rmin, rmax = solve(root.right)

            ivalid = lmax < root.val < rmin and lvalid and rvalid

            return ivalid, min(root.val, lmin, rmin), max(root.val, lmax, rmax)
        
        return solve(root)[0]

