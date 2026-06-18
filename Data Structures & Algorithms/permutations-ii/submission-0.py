class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used = [False] * len(nums)
        nums.sort()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i] or (i > 0 and not used[i-1] and nums[i] == nums[i-1]):
                    continue
                
                path.append(nums[i])
                used[i] = True

                backtrack(path)

                path.pop()
                used[i] = False
        
        backtrack([])

        return res