class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dq = deque()
        visited = set()
        dq.append("0000")
        visited.add("0000")
        deadends = set(deadends)
        count = 0

        if dq[0] in deadends:
            return -1
            
        while dq:
            size = len(dq)

            for _ in range(size):
                code = dq.popleft()

                if code == target:
                    return count
                    
                code_list = list(code)
                
                for i in range(4):
                    prev_code_i = code_list[i]

                    code_up_i = str((int(code_list[i]) + 1) % 10)
                    code_down_i = str((int(code_list[i]) - 1) % 10)

                    code_list[i] = code_up_i
                    code_up_str = "".join(code_list)

                    if code_up_str not in visited and code_up_str not in deadends:
                        dq.append(code_up_str)
                        visited.add(code_up_str)

                    code_list[i] = code_down_i
                    code_down_str = "".join(code_list)

                    if code_down_str not in visited and code_down_str not in deadends:
                        dq.append(code_down_str)
                        visited.add(code_down_str)

                    code_list[i] = prev_code_i

            count += 1
        
        return -1