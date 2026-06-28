# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0)
            if not node.left and not node.right:
                return (node.val, 0)
            
            stole_left, not_stole_left = dfs(node.left)
            stole_right, not_stole_right = dfs(node.right)

            return (node.val + not_stole_left + not_stole_right, max(stole_left, not_stole_left) + max(stole_right, not_stole_right))
        
        return max(dfs(root))