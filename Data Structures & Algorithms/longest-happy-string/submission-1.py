import heapq

class Solution(object):
    def longestDiverseString(self, a, b, c):
        res = []
        heap = []

        for cnt, ch in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if cnt > 0:
                heapq.heappush(heap, (-cnt, ch))

        while heap:
            cnt, ch = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == ch and res[-2] == ch:
                if not heap:
                    break

                cnt2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                cnt2 += 1

                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))

                heapq.heappush(heap, (cnt, ch))

            else:
                res.append(ch)
                cnt += 1

                if cnt < 0:
                    heapq.heappush(heap, (cnt, ch))

        return ''.join(res)