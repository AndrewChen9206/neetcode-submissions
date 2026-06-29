class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while max_heap:
            neg_first = heapq.heappop(max_heap)
            
            if not max_heap:
                return -neg_first
            
            neg_second = heapq.heappop(max_heap)

            if neg_first != neg_second:
                heapq.heappush(max_heap, -(abs(neg_first - neg_second)))
        
        return 0