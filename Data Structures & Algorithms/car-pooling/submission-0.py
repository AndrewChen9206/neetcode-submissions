class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        passenger_dict = defaultdict(int)

        for passengers, from_i, to_i in trips:
            passenger_dict[from_i] += passengers
            passenger_dict[to_i] -= passengers
        
        current_passengers = 0

        for pos in sorted(passenger_dict):
            current_passengers += passenger_dict[pos]
            if current_passengers > capacity:
                return False
        
        return True