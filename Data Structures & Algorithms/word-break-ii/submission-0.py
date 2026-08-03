class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        words = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [[]]

            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word not in words:
                    continue
                
                for suffix in dfs(end):
                    sentences.append([word] + suffix)
                
            memo[start] = sentences

            return sentences
        
        return [' '.join(parts) for parts in dfs(0)]