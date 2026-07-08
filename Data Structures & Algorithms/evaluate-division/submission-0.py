class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)
        visited = set()
        res = []

        def dfs(curr, target, product):
            if curr == target:
                return product
            
            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor in visited:
                    continue

                ans = dfs(neighbor, target, product * weight)

                if ans != -1:
                    return ans
            
            return -1

        for i, equation in enumerate(equations):
            u, v = equation
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
        
        for u, v in queries:
            if u not in graph or v not in graph:
                res.append(-1)
                continue
            
            visited = set()
            res.append(dfs(u, v, 1))
                
        return res