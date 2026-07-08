class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        farthest_index_dict = {}
        index = []
        res = []

        for i, char in enumerate(s):
            farthest_index_dict[char] = i
        
        for i, char in enumerate(s):
            if not index or i > index[-1]:
                index.append(farthest_index_dict[char])
                continue
            
            index[-1] = max(index[-1], farthest_index_dict[char])

        for i in range(len(index)):
            if i == 0:
                res.append(index[i] + 1)
                continue
            
            res.append(index[i] - index[i-1])
        
        return res