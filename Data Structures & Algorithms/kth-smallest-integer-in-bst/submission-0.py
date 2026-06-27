# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.count = 0

        def inOrderDFS(node):
            if not node:
                return None
            
            ans = inOrderDFS(node.left)
            if ans is not None:
                return ans

            self.count += 1
            if self.count == k:
                return node.val

            ans = inOrderDFS(node.right)
            if ans is not None:
                return ans
        
        return inOrderDFS(root)