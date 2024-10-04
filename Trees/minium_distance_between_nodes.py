# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float('inf')
        def dfs(root):
            nonlocal prev, res
            if not root: 
                return 
            dfs(root.left)
            if prev is not None:
                res = min(res, root.val - prev.val)
            prev = root
            dfs(root.right)
        dfs(root)
        return res

class Solution2:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res= []
        min_val = float('inf')
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        l, r = 0, 1
        while r < len(res):
            min_val = min(min_val, res[r] - res[l])
            l += 1
            r += 1
        return min_val