class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def isEmpty(self):
        return self.head.next == self.tail

    def insertNode(self, node):
        temp_prev = self.tail.prev

        self.tail.prev = node
        node.next = self.tail

        node.prev = temp_prev
        temp_prev.next = node

    def deleteNode(self, node):
        temp_next = node.next
        temp_prev = node.prev

        temp_next.prev = temp_prev
        temp_prev.next = temp_next

        node.next = None
        node.prev = None
    
    def popLRU(self):
        lru_node = self.head.next
        temp_next = lru_node.next

        temp_next.prev = self.head
        self.head.next = temp_next

        return lru_node

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.freq_to_list = defaultdict(DoublyLinkedList)
        self.key_to_node = {}
        self.min_freq = float('inf')
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_node:
            return -1
        
        self.update(key)

        return self.key_to_node[key].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.update(key)
            return

        if len(self.key_to_node) == self.capacity:
            lru_node = self.freq_to_list[self.min_freq].popLRU()
            del self.key_to_node[lru_node.key]

        self.key_to_node[key] = Node(key=key, val=value)
        self.min_freq = 1
        self.freq_to_list[self.min_freq].insertNode(self.key_to_node[key])

    def update(self, key):
        node = self.key_to_node[key]
        freq = node.freq

        self.freq_to_list[freq].deleteNode(node)

        if self.freq_to_list[freq].isEmpty() and self.min_freq == freq:
            self.min_freq += 1

        node.freq += 1
        self.freq_to_list[node.freq].insertNode(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)