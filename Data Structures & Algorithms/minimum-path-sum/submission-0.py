class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[float('inf')] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        dp[0][1] = 0
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])

        return dp[len(grid)][len(grid[0])]