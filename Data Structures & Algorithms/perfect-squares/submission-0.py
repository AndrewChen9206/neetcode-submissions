class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        perfect = []

        for i in range(1, n+1):
            if i**2 > n:
                break
            
            perfect.append(i**2)
        
        for i in range(1, n+1):
            for per in perfect:
                if i >= per:
                    dp[i] = min(dp[i], dp[i-per] + 1)
                else:
                    break
        
        return dp[n]