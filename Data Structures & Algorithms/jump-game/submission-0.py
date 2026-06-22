class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest = nums[0]

        for idx in range(1, len(nums)):
            if idx <= furthest:
                furthest = max(furthest, idx + nums[idx])
                if furthest >= len(nums) - 1:
                    return True
            else:
                return False
        
        return True