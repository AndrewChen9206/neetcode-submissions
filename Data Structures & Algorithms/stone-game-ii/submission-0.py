class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)

        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]

        memo = {}

        def dfs(i, M):
            if i + 2 * M >= n:
                return piles[i]

            if (i, M) in memo:
                return memo[(i, M)]

            res = 0

            for X in range(1, 2 * M + 1):
                opponent = dfs(i + X, max(M, X))
                res = max(res, piles[i] - opponent)

            memo[(i, M)] = res
            return res

        return dfs(0, 1)