class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        compare = defaultdict(int)

        for i in range(len(order)):
            compare[order[i]] = i

        for i in range(1, len(words)):
            flag = 0
            
            for j in range(min(len(words[i-1]), len(words[i]))):
                if compare[words[i-1][j]] > compare[words[i][j]]:
                    return False
                elif compare[words[i-1][j]] < compare[words[i][j]]:
                    flag = 1
                    break
            
            if flag != 1 and len(words[i-1]) > len(words[i]):
                return False
        
        return True