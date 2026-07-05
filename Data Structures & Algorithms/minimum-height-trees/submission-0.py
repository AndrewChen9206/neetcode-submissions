class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        elif n == 2:
            return edges[0]

        degree = defaultdict(int)
        graph = defaultdict(list)
        dq = deque()
        remaining = n

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            graph[u].append(v)
            graph[v].append(u)
        
        for u, out in degree.items():
            if out == 1:
                dq.append(u)
        
        while remaining > 2:
            size = len(dq)
            remaining -= size

            for _ in range(size):
                leaf = dq.popleft()
                degree[leaf] = 0
                
                for neighbor in graph[leaf]:
                    if degree[neighbor] > 0:
                        degree[neighbor] -= 1
                        if degree[neighbor] == 1:
                            dq.append(neighbor)
            
        res = []

        while dq:
            res.append(dq.popleft())

        return res