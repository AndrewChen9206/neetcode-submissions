# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            self.res = max(self.res, node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        
        return self.res