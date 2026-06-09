# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # pre-order traversal
        ss = []
        def dfs(node):
            if not node:
                ss.append('#')
                return
            
            ss.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        sss = ','.join(ss)
        # print(sss)
        return sss
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ss = data.split(',')
        def build(i):
            if ss[i] == '#':
                return None, 1
            
            node = TreeNode(int(ss[i]))

            node.left, ln = build(i + 1)
            node.right, rn = build(i + 1 + ln)

            return node, 1 + ln + rn
        
        return build(0)[0]
