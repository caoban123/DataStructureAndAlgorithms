class Node:
    def __init__(self, data, weight = 0):
        self.weight = weight
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_head(self, data, weight):
        new_node = Node(data, weight)
        new_node.next = self.head
        self.head = new_node
    def print(self):
        current = self.head
        while current:
            print(f"Data: {current.data}, Weight: {current.weight}", end = "--> " )
            current = current.next
        print(None)
def merge(lst1, lst2):
    dummy = Node(None, 0)
    tail = dummy
    p1 = lst1.head
    p2 = lst2.head
    while p1 and p2:
        if p1.data < p2.data:
            tail.next = Node(p1.data, p1.weight)
            p1 = p1.next
        elif p1.data > p2.data:
            tail.next = Node(p2.data, p2.weight)
            p2 = p2.next
        else: 
            tail.next = Node(p1.data, p1.weight + p2.weight)
            p1 = p1.next
            p2 = p2.next
        tail = tail.next
    while p1:
        tail.next = Node(p1.data, p1.weight)
        tail = tail.next
        p1 = p1.next
    while p2:
        tail.next = Node(p2.data, p2.weight)
        tail = tail.next
        p2 = p2.next
    lst1.head = dummy.next




lst1 = LinkedList()
lst2 = LinkedList()
lst1.add_head(7, 5)
lst1.add_head(4, 3)
lst1.add_head(2, 2)
lst1.add_head(1, 4)
lst2.add_head(8, 4)
lst2.add_head(7, 1)
lst2.add_head(3, 7)
lst2.add_head(2, 3)


merge(lst1, lst2)
lst1.print()