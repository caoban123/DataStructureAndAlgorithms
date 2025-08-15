class HashNode:
    def __init__(self, key : str, value : int):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    def __init__(self, HashSize):
        self.capacity = HashSize
        self.table = [None] * self.capacity
    def __del__(self):
        self.table = [None] * self.capacity
    def _hash(self, key):
        return hash(key) % self.capacity
    def add(self,key,value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = HashNode(key, value)
        else:
            head = self.table[index]
            cur = head
            while cur:
                if cur.key == key:
                    cur.value = value
                    return
                cur = cur.next
            new_node = HashNode(key, value)
            new_node.next = head
            self.table[index] = new_node
    def search(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        else:
            head = self.table[index]
            cur = head
            while cur:
                if cur.key == key:
                    return cur.value
                cur = cur.next
            return None
    def remove(self,key):
        index = self._hash(key)
        if self.table[index] is None:
            return
        else:
            if self.table[index].key == key:
                self.table[index] = self.table[index].next
            else:
                head = self.table[index]
                cur = head
                while cur.next:
                    if cur.next.key == key:
                        break
                    cur = cur.next
                cur.next = cur.next.next
    def print(self):
        for i, head in enumerate(self.table):
            print(f"[{i}]", end=" ")
            cur = head
            while cur:
                print(f"--> {cur.key} : {cur.value}", end=" ")
                cur = cur.next
            print()  


if __name__ == "__main__":
    ht = HashTable(10)

    ht.add("apple", 3)
    ht.add("banana", 5)
    ht.add("cherry", 10)

    print("Value for 'apple':", ht.search("apple"))      # 3
    print("Value for 'banana':", ht.search("banana"))    # 5
    print("Value for 'grape':", ht.search("grape"))      # None

    ht.add("banana", 8)
    print("Updated value for 'banana':", ht.search("banana"))  # 8

    ht.print()
    ht.remove("banana")
    print("------------------------")
    ht.print()

    