class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)

        return max_sum