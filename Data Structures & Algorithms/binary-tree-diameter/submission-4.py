# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(node) -> list[int, int]:
            if not node:
                return (0, 0)
            
            ldia, ldpt = solve(node.left)
            rdia, rdpt = solve(node.right)

            max_dia = max(ldpt + rdpt, ldia, rdia)
            my_depth = 1 + max(ldpt, rdpt)
            return (max_dia, my_depth)

        return solve(root)[0]