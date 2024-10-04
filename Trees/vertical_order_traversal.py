# Definition for a binary tree node.
from collections import defaultdict
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        table = defaultdict(list)
        q = collections.deque()
        q.append([root,0])
        col_min = 0
        col_max = 0
        while q:
            node, col = q.popleft()
            if node.left: q.append([node.left, col - 1])
            if node.right: q.append([node.right, col + 1])
            table[col].append(node.val)
            col_min = min(col_min, col)
            col_max = max(col_max, col)
        res = []
        # print(table, col_min, col_max)
        for x in range(col_min, col_max + 1):
            res.append(table[x])
        return res
