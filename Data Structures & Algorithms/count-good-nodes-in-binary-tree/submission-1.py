# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, max_seen: int = -101) -> int:
        if not root: return 0

        l = self.goodNodes(root.left, max(max_seen, root.val))
        r = self.goodNodes(root.right, max(max_seen, root.val))

        if max_seen <= root.val:
            return 1 + l + r

        return l + r