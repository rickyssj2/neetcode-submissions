# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST: inorder traversal of BST gives the sorted order
        arr = [-1001]
        def inorder(node):
            if not node: return True

            if inorder(node.left) == False: 
                return False
            if arr[-1] >= node.val:
                return False
            arr.append(node.val)

            return inorder(node.right)
        
        return inorder(root)

