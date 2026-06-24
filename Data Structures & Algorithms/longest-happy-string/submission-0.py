class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        res = ""
        max_heap = []
        restricted = ''
        heapq.heappush(max_heap, (-a, 'a'))
        heapq.heappush(max_heap, (-b, 'b'))
        heapq.heappush(max_heap, (-c, 'c'))
        
        while True:
            neg_max_val, max_ch = heapq.heappop(max_heap)

            if neg_max_val == 0:
                    break
            
            if neg_max_val <= -2 and max_ch != restricted:
                res += max_ch + max_ch
                neg_max_val += 2
                restricted = max_ch
            elif neg_max_val > -2 and max_ch != restricted:
                res += max_ch
                neg_max_val += 1
                restricted = ""
            else:
                neg_second_val, second_ch = heapq.heappop(max_heap)

                if neg_second_val == 0:
                    break

                res += second_ch
                neg_second_val += 1
                restricted = ""
                heapq.heappush(max_heap, (neg_second_val, second_ch))
            
            heapq.heappush(max_heap, (neg_max_val, max_ch))

        return res