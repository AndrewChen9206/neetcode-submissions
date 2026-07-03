class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        dist_to_k = [float('inf')] * (n + 1)
        dist_to_k[k] = dist_to_k[0] = 0
        min_heap = [(0, k)]
        path_dict = {}

        for time in times:
            if time[0] not in path_dict:
                path_dict[time[0]] = [(time[1], time[2])]
            else:
                path_dict[time[0]].append((time[1], time[2]))
        
        if k not in path_dict:
            return -1

        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)

            if curr_dist > dist_to_k[u]:
                continue

            for v, w in path_dict.get(u, []):
                new_dist = curr_dist + w

                if new_dist < dist_to_k[v]:
                    dist_to_k[v] = new_dist
                    heapq.heappush(min_heap, (new_dist, v))
        
        return max(dist_to_k) if float('inf') not in dist_to_k else -1