# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder(node) -> bool: # True: keep traversing, False stop traversing
            if not node: return True

            if inorder(node.left) == False:
                return False
            if len(arr) == k:
                return False
            arr.append(node.val)
            return inorder(node.right)
        
        inorder(root)

        return arr[-1]