class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stk = []
        str_stk = []
        curr_str = ""
        curr_num = 0

        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            elif s[i] == '[':
                num_stk.append(curr_num)
                str_stk.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif s[i].isalpha():
                curr_str += s[i]
            else:
                repeat_times = num_stk.pop()
                prev_str = str_stk.pop()
                curr_str = prev_str + repeat_times * curr_str
        
        return curr_str