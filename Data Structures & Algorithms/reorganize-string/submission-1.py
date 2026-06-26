class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_heap = []
        counter = defaultdict(int)
        res = []

        for val in s:
            counter[val] += 1
        
        for val, freq in counter.items():
            heapq.heappush(max_heap, (-freq, val))

        while max_heap:
            neg_freq, val = heapq.heappop(max_heap)

            if len(res) > 0 and val == res[-1]:
                if not max_heap:
                    return ""
                
                second_neg_freq, second_val = heapq.heappop(max_heap)
                res.append(second_val)

                if second_neg_freq + 1 != 0:
                    heapq.heappush(max_heap, (second_neg_freq + 1, second_val))
                
                heapq.heappush(max_heap, (neg_freq, val))

                continue
            
            res.append(val)

            if neg_freq + 1 != 0:
                heapq.heappush(max_heap, (neg_freq + 1, val))
        
        return "".join(res)
