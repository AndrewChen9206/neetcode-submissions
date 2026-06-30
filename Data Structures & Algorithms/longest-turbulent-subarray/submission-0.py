class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        turbulent = 1
        curr_len = 0
        curr_sign = '='

        if len(arr) == 1:
            return turbulent

        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                if curr_sign == '>':
                    curr_len += 1
                else:
                    curr_len = 2
                
                curr_sign = '<'
            elif arr[i] > arr[i-1]:
                if curr_sign == '<':
                    curr_len += 1
                else:
                    curr_len = 2
                
                curr_sign = '>'
            else:
                curr_len = 1
                curr_sign = '='
            
            turbulent = max(turbulent, curr_len)
        
        return turbulent