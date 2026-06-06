# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l, r = self.maxDepth(root.left), self.maxDepth(root.right)

        return max(l, r) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l, r = self.maxDepth(root.left), self.maxDepth(root.right)

        return max(l + r, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        # return max(diamter passing thorugh me, max diameter in left subtree, max diameter in right subtree)