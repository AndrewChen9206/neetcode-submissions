class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)

        def canMinimize(limit):
            split = 1
            curr_num = 0

            for num in nums:
                if num + curr_num > limit:
                    curr_num = 0
                    split += 1
                
                curr_num += num
            
            return split <= k
        
        while left <= right:
            mid = (left + right) // 2

            if canMinimize(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left