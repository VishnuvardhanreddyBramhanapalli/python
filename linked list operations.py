class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_linkedlist(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def sort(self):
        if self.head is None:
            print("List is empty.")
            return
        arr = self.to_list()
        arr.sort()
        self.from_list(arr)

    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1
ll = LinkedList()
ll.insert_at_end(30)
ll.insert_at_end(10)
ll.insert_at_end(40)
ll.insert_at_end(20)
print("Before sorting:")
ll.print_linkedlist()
ll.sort()
print("After sorting:")
ll.print_linkedlist()
print("Index of 20:", ll.search(20))
print("Index of 50 (not in list):", ll.search(50))