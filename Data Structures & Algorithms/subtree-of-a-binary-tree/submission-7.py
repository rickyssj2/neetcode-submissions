# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, preorder):
            if not node:
                preorder.append('#')
                return
            
            preorder.append(str(node.val))
            dfs(node.left, preorder)
            dfs(node.right, preorder)
        
        # serialize root
        root_list = []
        dfs(root, root_list)
        # print(root_list)

        # serialize subroot
        subroot_list = []
        dfs(subRoot, subroot_list)
        # print(subroot_list)

        substr, rootstr = ','.join(subroot_list), ','.join(root_list)
        print(substr, rootstr)
        return substr in rootstr