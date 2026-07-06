class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row = len(heights)
        col = len(heights[0])

        def canReach(limit):
            visited = [[False] * col for _ in range(row)]
            dq = deque()

            dq.append((0, 0))
            visited[0][0] = True

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while dq:
                x, y = dq.popleft()

                if x == row - 1 and y == col - 1:
                    return True

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or nx >= row or ny < 0 or ny >= col:
                        continue

                    if visited[nx][ny]:
                        continue

                    if abs(heights[nx][ny] - heights[x][y]) <= limit:
                        visited[nx][ny] = True
                        dq.append((nx, ny))

            return False
        
        left = 0
        right = 10**6

        while left < right:
            target = (left + right) // 2

            if canReach(target):
                right = target
            else:
                left = target + 1
        
        return left