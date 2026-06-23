class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        gain = [0] * len(gas)

        for i in range(len(gain)):
            gain[i] = gas[i] - cost[i]
        
        start = curr = tank = 0

        for curr in range(len(gain)):
            if tank + gain[curr] < 0:
                start = (curr + 1) % len(gain)
                tank = 0
            else:
                tank += gain[curr]
        
        return start