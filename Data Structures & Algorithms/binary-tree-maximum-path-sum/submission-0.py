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
                return float('-inf')
            if not node.left and not node.right:
                return node.val
            
            left_optimal = dfs(node.left)
            right_optimal = dfs(node.right)
            self.res = max(self.res, node.val, node.val + left_optimal, node.val + right_optimal, left_optimal, right_optimal, node.val + left_optimal + right_optimal)

            return max(node.val, node.val + left_optimal, node.val + right_optimal)

        return max(dfs(root), self.res)