class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval[0])
        result = []

        for left, right in intervals:
            if not result or result[-1][1] < left:
                result.append([left, right])
            else:
                result[-1][1] = max(result[-1][1], right)

        return result