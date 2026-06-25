class Node(object):
    def __init__(self, key=-1, value=-1, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.LRUdict = {}
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def updatePosition(self, key):
        self.LRUdict[key].prev.nxt = self.LRUdict[key].nxt
        self.LRUdict[key].nxt.prev = self.LRUdict[key].prev
        self.tail.prev.nxt = self.LRUdict[key]
        self.LRUdict[key].prev = self.tail.prev
        self.LRUdict[key].nxt = self.tail
        self.tail.prev = self.LRUdict[key]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.LRUdict:
            self.updatePosition(key)
            return self.LRUdict[key].value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.LRUdict:
            if len(self.LRUdict) == self.size:
                del self.LRUdict[self.head.nxt.key]
                self.head.nxt = self.head.nxt.nxt
                self.head.nxt.prev = self.head

            new_node = Node(key=key, value=value)
            self.tail.prev.nxt = new_node
            new_node.prev = self.tail.prev
            new_node.nxt = self.tail
            self.tail.prev = new_node
            self.LRUdict[key] = new_node
        else:
            self.LRUdict[key].value = value
            self.updatePosition(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)