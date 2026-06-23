class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        return start