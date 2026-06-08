# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        rootval = preorder[0]
        lstn = 0

        # 1 + lstn + rstn = n

        for i, v in enumerate(inorder):
            if v == rootval:
                lstn = i
                break
        
        rstn = len(preorder) - lstn - 1

        # pre = [4, 2, 1, 3, 6, 5, 7] 
        # ino = [1, 2, 3, 4, 5, 6, 7] 

        lst = self.buildTree(preorder[1: 1 + lstn], inorder[:lstn])
        rst = self.buildTree(preorder[1 + lstn:], inorder[1 + lstn:])

        root = TreeNode(rootval)
        root.left, root.right = lst, rst
        return root