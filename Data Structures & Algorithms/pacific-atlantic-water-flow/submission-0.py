class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        row = len(heights)
        col = len(heights[0])
        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]

        def dfs(visited, height, i, j):
            if i < 0 or i >= row or j < 0 or j >= col:
                return
            if visited[i][j]:
                return

            if heights[i][j] >= height:
                visited[i][j] = True
                
                dfs(visited, heights[i][j], i-1, j)
                dfs(visited, heights[i][j], i+1, j)
                dfs(visited, heights[i][j], i, j-1)
                dfs(visited, heights[i][j], i, j+1)
        
        for i in range(row):
            dfs(pacific, 0, i, 0)
            dfs(atlantic, 0, i, col-1)
        
        for j in range(col):
            dfs(pacific, 0, 0, j)
            dfs(atlantic, 0, row-1, j)

        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        
        return res