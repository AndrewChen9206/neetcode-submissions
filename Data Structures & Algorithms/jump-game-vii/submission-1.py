class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        dp = [False] * n
        dp[0] = True

        reachable_count = 0

        for i in range(1, n):
            if i - minJump >= 0 and dp[i - minJump]:
                reachable_count += 1

            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable_count -= 1

            if s[i] == '0' and reachable_count > 0:
                dp[i] = True

        return dp[-1]