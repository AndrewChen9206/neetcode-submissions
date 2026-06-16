class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum_min = curr_sum_max = nums[0]
        sub_min = sub_max = nums[0]
        total = sum(nums)

        for val in nums[1:]:
            curr_sum_min = min(val, curr_sum_min + val)
            curr_sum_max = max(val, curr_sum_max + val)
            sub_min = min(sub_min, curr_sum_min)
            sub_max = max(sub_max, curr_sum_max)
        
        if total - sub_min == 0:
            return sub_max
        else:
            return max(sub_max, total - sub_min)