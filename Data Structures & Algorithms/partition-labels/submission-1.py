class Solution(object):
    def partitionLabels(self, s):
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        res = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res