# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        lsame = self.isSameTree(p.left, q.left)
        rsame = self.isSameTree(p.right, q.right)
        
        cursame = lsame and rsame and p.val == q.val

        return cursame

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        lsub = self.isSubtree(root.left, subRoot)
        if lsub:
            return True
        rsub = self.isSubtree(root.right, subRoot)
        if rsub:
            return True

        cursame = False
        if root.val == subRoot.val:
            cursame = self.isSameTree(root, subRoot) 
        return cursame


        # tree (N), query(M)
        # N + M
        