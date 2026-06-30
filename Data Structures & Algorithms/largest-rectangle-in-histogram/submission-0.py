class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 1:
            return heights[0]

        res = 0

        def buildLeftless(heights, is_reverse):
            left_min_index = [0] * len(heights)
            left_min_index[0] = -1
            mono_stk = [0]

            for i in range(1, len(heights)):
                while mono_stk and heights[mono_stk[-1]] >= heights[i]:
                    mono_stk.pop()
                
                if not mono_stk:
                    left_min_index[i] = -1
                else:
                    left_min_index[i] = mono_stk[-1]
                
                mono_stk.append(i)

            if is_reverse:
                for i in range(len(heights)):
                    left_min_index[i] = len(heights) - left_min_index[i] - 1
            
            return left_min_index if not is_reverse else left_min_index[::-1]
        
        left_min_index = buildLeftless(heights, False)
        right_min_index = buildLeftless(heights[::-1], True)

        for i in range(len(heights)):
            width = right_min_index[i] - left_min_index[i] - 1
            res = max(res, heights[i] * width)
        
        return res
