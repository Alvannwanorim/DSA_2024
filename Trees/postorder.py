# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            traverse(root.right)
            res.append(root.val)
        traverse(root)
        return res 