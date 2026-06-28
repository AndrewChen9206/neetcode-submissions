class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = defaultdict(int)
        window = defaultdict(int)
        matched = 0
        res = ""

        for val in t:
            target[val] += 1
        
        left = right = 0

        while right < len(s):
            if s[right] in target:
                window[s[right]] += 1
                
                if window[s[right]] <= target[s[right]]:
                    matched += 1
            
            while matched == len(t):
                if res == "":
                    res = s[left:right+1]
                else:
                    if (right - left + 1) < len(res):
                        res = s[left:right+1]

                if s[left] in target:
                    window[s[left]] -= 1
                    
                    if window[s[left]] < target[s[left]]:
                        matched -= 1
                
                left += 1

            right += 1
        
        return res