# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
            
        res = []
        dq = deque()
        dq.append(root)

        while dq:
            size = len(dq)
            res.append(dq[-1].val)

            for _ in range(size):
                node = dq.popleft()
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        
        return res