class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = 1
        res = 1

        for j in range(1, len(nums)):
            longest = 0

            for i in range(j, -1, -1):
                if nums[i] < nums[j]:
                    longest = max(longest, dp[i])
            
            dp[j] = longest + 1
            res = max(res, dp[j])

        return res