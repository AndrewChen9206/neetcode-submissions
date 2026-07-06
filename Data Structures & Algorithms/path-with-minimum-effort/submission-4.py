class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row = len(heights)
        col = len(heights[0])

        dist = [[float('inf')] * col for _ in range(row)]
        dist[0][0] = 0
        
        min_heap = [(0, 0, 0)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            effort, x, y = heapq.heappop(min_heap)

            if x == row - 1 and y == col - 1:
                return effort

            if effort > dist[x][y]:
                continue

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    continue
                
                diff = abs(heights[nx][ny] - heights[x][y])
                new_effort = max(effort, diff)

                if new_effort < dist[nx][ny]:
                    dist[nx][ny] = new_effort
                    heapq.heappush(min_heap, (new_effort, nx, ny))
            
        return 0