class Solution(object):
    def simplifyPath(self, path):
        stk = []

        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(part)

        return '/' + '/'.join(stk)