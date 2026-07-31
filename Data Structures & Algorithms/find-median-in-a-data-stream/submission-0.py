class MedianFinder(object):

    def __init__(self):
        self.smaller_nums = []
        self.larger_nums = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.smaller_nums, -num)
        heapq.heappush(self.larger_nums, -heapq.heappop(self.smaller_nums))

        if len(self.larger_nums) > len(self.smaller_nums):
            heapq.heappush(self.smaller_nums, -heapq.heappop(self.larger_nums))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.smaller_nums) > len(self.larger_nums):
            return -self.smaller_nums[0]

        return (-self.smaller_nums[0] + self.larger_nums[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()