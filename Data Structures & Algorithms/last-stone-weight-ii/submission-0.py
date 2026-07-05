class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        closest_to_half = 0

        for stone in stones:
            for i in range(target, -1, -1):
                if i >= stone:
                    dp[i] = dp[i] or dp[i-stone]
                    if dp[i]:
                        closest_to_half = max(closest_to_half, i)
        
        return (total - closest_to_half) - closest_to_half