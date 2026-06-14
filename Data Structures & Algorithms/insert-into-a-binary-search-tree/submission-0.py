# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val=val)
            
        def dfs(node):
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val=val)
                    return
                dfs(node.left)
            else:
                if not node.right:
                    node.right = TreeNode(val=val)
                    return
                dfs(node.right)
        
        dfs(root)

        return root