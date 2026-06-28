class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        dq_R = deque()
        dq_D = deque()

        for i, party in enumerate(senate):
            if party == 'R':
                dq_R.append(i)
            else:
                dq_D.append(i)

        while dq_R and dq_D:
            n = max(dq_R[-1], dq_D[-1]) + 1
            R = dq_R.popleft()
            D = dq_D.popleft()

            if R < D:
                dq_R.append(n)
            else:
                dq_D.append(n)
        
        return "Radiant" if dq_R else "Dire"