class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        water = 0

        while left < right:
            if leftMax < rightMax:
                water += leftMax - height[left]
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                water += rightMax - height[right]
                right -= 1
                rightMax = max(rightMax, height[right])
        
        return water