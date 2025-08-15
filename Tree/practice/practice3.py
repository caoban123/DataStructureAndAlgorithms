class HashNode:
    def __init__(self, key : str, value : int):
        self.key = key
        self.value = value
class HashTable:
    def __init__(self, HashSize: int):
        self.capacity = HashSize
        self.table = [None] * self.capacity
        self.deleted = HashNode("Delete", -1)
    def __del__(self):
        self.table = [None] * self.capacity
    def _hash(self, key, index):
        return (hash(key) + index) % self.capacity
    def add(self, key, value):
        for i in range(self.capacity):
            index = self._hash(key, i)
            if self.table[index] is None or self.table[index] == self.deleted:
                self.table[index] = HashNode(key, value)
                return
            elif self.table[index].key == key:
                self.table[index].value = value
                return
        print("table is full")
    def searchValue(self, key):
        for i in range(self.capacity):
            index = self._hash(key, i)
            if self.table[index] is None:
                return None
            elif self.table[index] == self.deleted:
                continue
            elif self.table[index].key == key:
                return self.table[index].value 
        return None
    def remove(self, key):
        for i in range(self.capacity):
            index = self._hash(key, i)
            if self.table[index] is None:
                return
            if self.table[index] == self.deleted:
                continue
            if self.table[index].key == key:
                self.table[index] = self.deleted
                return
    def printTable(self):
        for i in range(self.capacity):
            if self.table[i] is not None:
                print(f"Index {i}: Key = {self.table[i].key}, Value = {self.table[i].value}")
            else:
                print(f"Index {i}: Empty")
if __name__ == "__main__":
    ht = HashTable(10)

    ht.add("apple", 3)
    ht.add("banana", 5)
    ht.add("cherry", 10)

    print("Value for 'apple':", ht.searchValue("apple"))      # 3
    print("Value for 'banana':", ht.searchValue("banana"))    # 5
    print("Value for 'grape':", ht.searchValue("grape"))      # None

    ht.add("banana", 8)
    print("Updated value for 'banana':", ht.searchValue("banana"))  # 8
    ht.printTable()
    ht.remove("apple")
    print("Value for 'apple' after removal:", ht.searchValue("apple"))  # None
    ht.printTable()

            

