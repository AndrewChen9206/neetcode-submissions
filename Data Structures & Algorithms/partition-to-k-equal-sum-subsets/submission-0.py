class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)

        if total % k != 0:
            return False
        
        target = total // k

        bucket = [0] * k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        def backtrack(i):
            if i == len(nums):
                return True

            num = nums[i]

            for j in range(k):
                if num + bucket[j] > target:
                    continue

                if j > 0 and bucket[j] == bucket[j-1]:
                    continue

                bucket[j] += num

                if backtrack(i+1):
                    return True

                bucket[j] -= num

            return False

        return backtrack(0)