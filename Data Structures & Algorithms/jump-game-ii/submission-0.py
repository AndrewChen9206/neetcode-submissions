class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        step = 0
        i = 0

        while i < len(nums):
            best_reach = 0
            best_idx = 0

            step += 1

            for idx in range(i+1, i+nums[i]+1):
                if idx >= len(nums) - 1:
                    return step
                if idx + nums[idx] >= best_reach:
                    best_reach = idx + nums[idx]
                    best_idx = idx
            
            i = best_idx
        
        return step