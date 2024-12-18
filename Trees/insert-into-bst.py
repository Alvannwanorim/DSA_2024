# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        prev = None
        curr= root
        while curr:
            if val > curr.val:
                prev = curr
                curr = curr.right
            else:
                prev = curr
                curr = curr.left
        if val < prev.val:
            prev.left = node
        else:
            prev.right = node

        return root