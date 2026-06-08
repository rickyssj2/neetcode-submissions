# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST: inorder traversal of BST gives the sorted order
        arr= []
        def inorder(node):
            if not node: return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)

        return arr == sorted(arr) and len(arr) == len(set(arr))

