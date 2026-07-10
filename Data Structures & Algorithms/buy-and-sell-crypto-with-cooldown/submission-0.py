class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0] = [-prices[0], -float('inf'), 0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][2] - prices[i], dp[i-1][0])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        
        return max(dp[-1][1], dp[-1][2])
