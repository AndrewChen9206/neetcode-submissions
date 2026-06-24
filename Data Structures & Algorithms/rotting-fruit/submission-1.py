class Solution(object):
    def orangesRotting(self, grid):
        fresh = 0
        dq = deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    dq.append((r, c))

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq and fresh > 0:
            for _ in range(len(dq)):
                r, c = dq.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        dq.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1