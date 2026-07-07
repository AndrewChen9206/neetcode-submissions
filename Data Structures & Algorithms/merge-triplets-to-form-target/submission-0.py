class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        res = [False, False, False]
        
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                if triplet[0] == target[0]:
                    res[0] = True
                if triplet[1] == target[1]:
                    res[1] = True
                if triplet[2] == target[2]:
                    res[2] = True
            
            if all(res):
                return True

        return False