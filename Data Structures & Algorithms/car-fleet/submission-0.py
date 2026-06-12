class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed), reverse=True)

        res = 0
        curr_fleet_time = 0

        for pos, spd in cars:
            time = float(target - pos) / spd

            if time > curr_fleet_time:
                res += 1
                curr_fleet_time = time

        return res