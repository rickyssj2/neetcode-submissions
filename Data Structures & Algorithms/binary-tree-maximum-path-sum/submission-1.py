# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(node) -> list[int, int]:
            if not node:
                return (0, -math.inf)
            
            lpath, lmps = solve(node.left)
            rpath, rmps = solve(node.right)

            ipath = node.val + max(max(lpath, 0), max(rpath, 0))
            imps = node.val + max(lpath, 0) + max(rpath, 0)

            return ipath, max(imps, lmps, rmps)
        
        return solve(root)[1]
