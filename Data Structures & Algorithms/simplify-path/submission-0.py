class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk = []
        curr = ""

        path += '/'

        for i in range(len(path)):
            if path[i] == '/':
                if curr == ".." and stk:
                    stk.pop()
                elif curr != '' and curr != '.' and curr != "..":
                    stk.append(curr)
                curr = ""
            else:
                curr += path[i]
        
        return '/' + '/'.join(stk)