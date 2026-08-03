class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        prev_end = intervals[0][1]
        remove = 0

        for start, end in intervals[1:]:
            if prev_end <= start:
                prev_end = end
            else:
                prev_end = min(prev_end, end)
                remove += 1
        
        return remove
