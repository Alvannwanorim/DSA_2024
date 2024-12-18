# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            if not root:
                return 
            res.append("(")
            res.append(str(root.val))
            if root.right and not root.left:
                res.append("()")
            dfs(root.left)
            dfs(root.right)
            res.append(")")
        dfs(root)
        return "".join(res[1:-1])
        