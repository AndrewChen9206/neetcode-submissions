class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_left_paren = 0
        max_left_paren = 0

        for val in s:
            if val == '(':
                min_left_paren += 1
                max_left_paren += 1
            elif val == '*':
                min_left_paren = max(min_left_paren - 1, 0)
                max_left_paren += 1
            else:
                min_left_paren = max(min_left_paren - 1, 0)
                max_left_paren = max_left_paren - 1
                
                if max_left_paren < 0:
                    return False
        
        return min_left_paren == 0