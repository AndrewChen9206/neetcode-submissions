class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 保證 nums1 是比較短的，避免 j out of index
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        A, B = nums1, nums2
        m, n = len(A), len(B)

        total = m + n
        left_size = (total + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = left_size - i

            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")

            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return float(max(A_left, B_left))
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0

            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1