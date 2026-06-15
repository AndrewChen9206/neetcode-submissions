class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x + 1

        while left < right:
            mid = (left + right) // 2

            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        
        return left - 1