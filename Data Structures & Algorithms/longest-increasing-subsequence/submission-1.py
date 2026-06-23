class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []

        def lowerBound(left, right, target):
            while left < right:
                mid = (left + right) // 2

                if tails[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            return left
        
        for num in nums:
            swap_idx = lowerBound(0, len(tails), num)

            if swap_idx == len(tails):
                tails.append(num)
            else:
                tails[swap_idx] = num

        return len(tails)