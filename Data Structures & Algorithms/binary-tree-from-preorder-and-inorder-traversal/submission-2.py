class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        def solve(pl, pr, il, ir):
            # empty segment
            if pl > pr or il > ir:
                return None
            # single node
            if pl == pr:
                return TreeNode(preorder[pl])

            rootval = preorder[pl]

            # find root index in inorder
            root_in_inorder = il
            for i in range(il, ir + 1):
                if inorder[i] == rootval:
                    root_in_inorder = i
                    break

            # number of nodes in left subtree
            lstn = root_in_inorder - il
            # number of nodes in right subtree
            rstn = (pr - pl + 1) - 1 - lstn

            # left subtree:
            # preorder: [pl+1 .. pl+lstn]
            # inorder:  [il .. root_in_inorder-1]
            lst = solve(pl + 1, pl + lstn, il, root_in_inorder - 1)

            # right subtree:
            # preorder: [pl+lstn+1 .. pr]
            # inorder:  [root_in_inorder+1 .. ir]
            rst = solve(pl + lstn + 1, pr, root_in_inorder + 1, ir)

            root = TreeNode(rootval)
            root.left, root.right = lst, rst
            return root

        return solve(0, n - 1, 0, n - 1)