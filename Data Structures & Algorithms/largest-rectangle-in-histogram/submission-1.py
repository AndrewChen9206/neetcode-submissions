class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        leftLess = [-1] * n
        rightLess = [n] * n

        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                leftLess[i] = stack[-1]

            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                rightLess[i] = stack[-1]

            stack.append(i)

        res = 0

        for i in range(n):
            width = rightLess[i] - leftLess[i] - 1
            res = max(res, heights[i] * width)

        return res