class MyHashMap(object):

    def __init__(self):
        self.bucket = [[] for _ in range(1009)]
        self.bucket_count = 1009

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.bucket_count
        
        for pair in self.bucket[index]:
            if pair[0] == key:
                pair[1] = value
                break
        else:
            self.bucket[index].append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % self.bucket_count
        
        for pair in self.bucket[index]:
            if pair[0] == key:
                return pair[1]
        else:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.bucket_count
        
        for pair in self.bucket[index]:
            if pair[0] == key:
                self.bucket[index].remove(pair)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)