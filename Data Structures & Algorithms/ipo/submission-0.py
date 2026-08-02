class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        locked = []
        available = []

        for i in range(len(profits)):
            locked.append((capital[i], profits[i]))
        
        heapq.heapify(locked)

        for _ in range(k):
            while locked and locked[0][0] <= w:
                _, profit = heapq.heappop(locked)
                heapq.heappush(available, -profit)
            
            if not available:
                return w
            
            profit = -heapq.heappop(available)
            w += profit
        
        return w