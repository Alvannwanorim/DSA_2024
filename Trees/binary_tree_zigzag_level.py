# Definition for a binary tree node.
import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        level_count = 0
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level.append(node.val)
            level = reversed(level) if level_count % 2 else level
            level_count += 1
            res.append(level)
        return res