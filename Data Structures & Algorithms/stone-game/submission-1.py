class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[0] * len(piles) for _ in range(len(piles))]

        for i in range(len(piles)):
            dp[i][i] = piles[i]

        for length in range(1, len(piles)):
            for i in range(len(piles) - length):
                j = i + length
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        
        return dp[len(piles)-1][len(piles)-1] > 0