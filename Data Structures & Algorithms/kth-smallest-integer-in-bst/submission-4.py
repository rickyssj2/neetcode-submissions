# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = -1
        seen = 0
        def inorder(node) -> bool: # True: keep traversing, False stop traversing
            nonlocal kth, seen
            if not node: return True

            if inorder(node.left) == False:
                return False
            if seen == k:
                return False
            kth = node.val
            seen += 1
            return inorder(node.right)
        
        inorder(root)

        return kth