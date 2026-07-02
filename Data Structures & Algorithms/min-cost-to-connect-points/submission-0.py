class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0

        total = 0

        for _ in range(n):
            cur = -1

            for i in range(n):
                if not visited[i] and (cur == -1 or min_dist[i] < min_dist[cur]):
                    cur = i

            visited[cur] = True
            total += min_dist[cur]

            x1, y1 = points[cur]

            for i in range(n):
                if not visited[i]:
                    x2, y2 = points[i]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    min_dist[i] = min(min_dist[i], dist)

        return total