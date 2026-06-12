class TimeMap(object):

    def __init__(self):
        self.timemap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.timemap:
            self.timemap[key] = [(timestamp, value)]
        else:
            self.timemap[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.timemap:
            return ""

        left = 0
        right = len(self.timemap[key]) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.timemap[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return self.timemap[key][right][1] if right != -1 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)