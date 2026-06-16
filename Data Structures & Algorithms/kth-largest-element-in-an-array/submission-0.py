class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        if len(nums) == len(min_heap):
            return min_heap[0]

        for val in nums[k:]:
            heapq.heappush(min_heap, val)

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]