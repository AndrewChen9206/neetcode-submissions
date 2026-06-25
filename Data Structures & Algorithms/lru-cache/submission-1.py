class Node(object):
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.LRUdict = {}

        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def add_to_tail(self, node):
        prev_node = self.tail.prev

        prev_node.nxt = node
        node.prev = prev_node
        node.nxt = self.tail
        self.tail.prev = node

    def move_to_tail(self, node):
        self.remove(node)
        self.add_to_tail(node)

    def get(self, key):
        if key not in self.LRUdict:
            return -1

        node = self.LRUdict[key]
        self.move_to_tail(node)
        return node.value

    def put(self, key, value):
        if key in self.LRUdict:
            node = self.LRUdict[key]
            node.value = value
            self.move_to_tail(node)
            return

        if len(self.LRUdict) == self.capacity:
            lru = self.head.nxt
            self.remove(lru)
            del self.LRUdict[lru.key]

        new_node = Node(key, value)
        self.add_to_tail(new_node)
        self.LRUdict[key] = new_node