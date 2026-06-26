class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)

        def overCapacity(capacity):
            curr_weight = 0
            curr_days = 1

            for weight in weights:
                if curr_weight + weight > capacity:
                    curr_days += 1
                    curr_weight = 0
                
                curr_weight += weight
            
            return curr_days <= days
        
        while left <= right:
            capacity = (left + right) // 2

            if overCapacity(capacity):
                right = capacity - 1
            else:
                left = capacity + 1
        
        return left