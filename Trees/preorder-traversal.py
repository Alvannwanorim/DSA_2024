# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def traverse(root):
            if not root:
                return
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return res 
        