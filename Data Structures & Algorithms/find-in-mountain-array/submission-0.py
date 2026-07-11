# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        mountain_length = mountainArr.length()
        left = 0
        right = mountain_length - 1

        while left < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        top_idx = left

        left = 0
        right = top_idx

        while left <= right:
            mid = (left + right) // 2
            height = mountainArr.get(mid)

            if height == target:
                return mid
            elif height < target:
                left = mid + 1
            else:
                right = mid - 1
        
        left = top_idx
        right = mountain_length - 1

        while left <= right:
            mid = (left + right) // 2
            height = mountainArr.get(mid)

            if height == target:
                return mid
            elif height < target:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1