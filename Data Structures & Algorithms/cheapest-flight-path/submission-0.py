class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            new_dist = dist[:]

            for u, v, price in flights:
                if dist[u] == float('inf'):
                    continue
                
                new_dist[v] = min(new_dist[v], dist[u] + price)
            
            dist = new_dist
        
        return dist[dst] if dist[dst] != float('inf') else -1