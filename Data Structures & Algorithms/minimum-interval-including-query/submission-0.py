class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        sorted_queries = []

        for i, q in enumerate(queries):
            sorted_queries.append((q, i))
        
        sorted_queries.sort()

        res = [-1] * len(queries)
        min_heap = []
        i = 0
        n = len(intervals)

        for q, q_index in sorted_queries:
            while i < n and intervals[i][0] <= q:
                heapq.heappush(min_heap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                res[q_index] = min_heap[0][0]
            else:
                res[q_index] = -1

        return res