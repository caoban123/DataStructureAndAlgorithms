class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class Table:
    def __init__(self, hashSize):
        self.capacity = hashSize
        self.table = [None] * self.capacity
    def _Hash(self, key):
        return hash(key) % self.capacity
    def add(self, key, value):
        index = self._Hash(key)
        head = self.table[index]
        cur = head
        while cur:
            if cur.value == value:
                cur.value = value
                return
            cur = cur.next
        new_node = Node(key, value)
        new_node = Node(key, value)
        new_node.next = head
        self.table[index] = new_node

