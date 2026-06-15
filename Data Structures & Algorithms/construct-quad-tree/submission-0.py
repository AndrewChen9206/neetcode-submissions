"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def checkIsLeaf(row, col, size):
            first_val = grid[row][col]
            
            for r in range(row, row+size):
                for c in range(col, col+size):
                    if grid[r][c] != first_val:
                        return False
            
            return True
        
        def buildQuadTree(row, col, size):
            node = Node()

            if checkIsLeaf(row, col, size):
                node.val = grid[row][col]
                node.isLeaf = True
                
                return node
            
            half = size // 2
            
            node.topLeft = buildQuadTree(row, col, half)
            node.topRight = buildQuadTree(row, col + half, half)
            node.bottomLeft = buildQuadTree(row + half, col, half)
            node.bottomRight = buildQuadTree(row + half, col + half, half)
            
            return node
        
        return buildQuadTree(0, 0, len(grid))