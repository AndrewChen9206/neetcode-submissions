class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - k
        res = []

        while left < right:
            start = (left + right) // 2

            if (x - arr[start]) > (arr[start + k] - x):
                left = start + 1
            else:
                right = start
 
        return arr[left:left+k]