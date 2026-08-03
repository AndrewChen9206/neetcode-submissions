class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda interval: interval[0])
        result = []
        i = 0

        while i < len(intervals):
            left, right = intervals[i]

            while i + 1 < len(intervals) and right >= intervals[i+1][0]:
                right = max(right, intervals[i+1][1])
                i += 1
            
            result.append([left, right])

            i += 1
        
        return result
        