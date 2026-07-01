class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        edges_dict = defaultdict(list)
        visited = set()

        def dfs(current, target):
            if current == target:
                return True

            visited.add(current)

            for neighbor in edges_dict[current]:
                if neighbor not in visited and dfs(neighbor, target):
                    return True
            
            return False
        
        for a, b in edges:
            visited.clear()

            if dfs(a, b):
                return [a, b]

            edges_dict[a].append(b)
            edges_dict[b].append(a)