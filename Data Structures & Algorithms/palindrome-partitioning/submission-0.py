class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def checkPalindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                
                start += 1
                end -= 1
            
            return True
        
        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                if checkPalindrome(start, end):
                    path.append(s[start:end+1])
                    dfs(end + 1, path)
                    path.pop()
        
        dfs(0, [])
        
        return res