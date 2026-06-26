class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                    continue

            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                    
                total = nums[i] + nums[j]
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    if total + nums[left] + nums[right] > target:
                        right -= 1
                    elif total + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        
                        while right > left and nums[right] == nums[right+1]:
                            right -= 1
        
        return res