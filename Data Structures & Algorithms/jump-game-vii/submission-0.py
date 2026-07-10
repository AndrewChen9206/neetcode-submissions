class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        dp = [False] * len(s)
        dp[0] = True
        can_reach_options = 0

        for i in range(minJump, maxJump+1):
            if s[i] == '0':
                dp[i] = True
        
        if dp[len(s)-1]:
            return True
        
        for i in range(1, maxJump+1-minJump+1):
            if dp[i]:
                can_reach_options += 1

        for i in range(maxJump+1, len(s)):
            if can_reach_options > 0 and s[i] == '0':
                dp[i] = True
            if dp[i-minJump+1]:
                can_reach_options += 1
            if dp[i-maxJump]:
                can_reach_options -= 1

        return dp[len(s)-1]