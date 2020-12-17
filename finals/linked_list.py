class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        self.index = 0


class LinkedList:
    def __init__(self, head):
        self.head = Node(head, None)

    def print_data(self):
        current_node = self.head

        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def length(self):
        current_node = self.head
        num_nodes = 0

        while current_node.next != None:
            num_nodes += 1
            current_node = current_node.next

        num_nodes += 1
        return num_nodes

    def append(self, new_data):
        current_node = self.head
        index = 0

        while current_node.next != None:
            current_node = current_node.next
            index += 1

        current_node.next = Node(new_data, None)
        current_node.next.index = index + 1

    def push(self, new_data):
        former_head = self.head
        self.head = Node(new_data, None)

        while former_head.next != None:
            self.append(former_head.data)
            former_head = former_head.next

        self.append(former_head.data)

    def index(self, item):
        current = self.head

        while current != None:
            if current.data == item:
                return current.position

            else:
                current = current.next

    def get_node(self, index):
        current = self.head

        for i in range(index):
            current = current.next

        return current.data

    def delete(self, index):
        current_node = self.head
  
        for n in range(index):
            current_node = current_node.next

        for n in range(index, self.length() - 1):
            current_node.data = current_node.next.data

            if current_node.index == self.length() - 2:
                current_node.next = None

            current_node = current_node.next

    def insert(self, new_data, index):
        current_node = self.head

        for n in range(index):
            current_node = current_node.next

        for n in range(index, self.length() - 1):
            value = current_node.data
            next_value = current_node.next.data

            if n == index:
                current_node.data = new_data

            if current_node.next.data != None:
                current_node.next.data = value
                current_node = current_node.next
        
        self.append(next_value)

''''
A = Node(4, None)
print("Asserting 'data' for class 'Node'")
assert A.data == 4, "Incorrect output"
print("PASSED")

print("Asserting method 'next' for class 'Node'")
assert A.next == None, "Incorrect output"
print("PASSED")

B = Node(8, None)
A.next = B

print("Asserting 'next' for class 'Node'")
assert A.next.data == 8, "Incorrect output"
print("PASSED")

linked_list = LinkedList(4)

print("Asserting 'data' for class 'LinkedList'")
assert linked_list.head.data == 4, "Incorrect output"
print("PASSED")

linked_list.append(8)

print("Asserting 'append' for class 'LinkedList'")
assert linked_list.head.next.data == 8, "Incorrect output"
print("PASSED")

linked_list.append(9)

print("Asserting method 'print_data' for class 'LinkedList'")
linked_list.print_data()

print("Asserting method 'length' for class 'LinkedList'")
assert linked_list.length() == 3, "Incorrect output"
print("PASSED")

linked_list = LinkedList('b')
linked_list.append('e')
linked_list.append('f')
linked_list.push('a')

print("Asserting 'length' method for LinkedList")
assert linked_list.length() == 4, "Incorrect output"
print("PASSED")


print("Asserting method 'index' for LinkedList")
assert linked_list.head.index == 0, "Incorrect output"
print("PASSED")

print("Asserting method 'index' for LinkedList")
assert linked_list.head.next.index == 1, "Incorrect output"
print("PASSED")

print("Asserting method 'index' for LinkedList")
assert linked_list.head.next.next.index == 2, "Incorrect output"
print("PASSED")

print("Asserting method 'index' for LinkedList")
assert linked_list.head.next.next.next.index == 3, "Incorrect output"
print("PASSED")

print("Asserting method 'get_node'")
assert linked_list.get_node(0) == 'a', "Incorrect output"
print("PASSED")

print("Asserting method 'get_node'")
assert linked_list.get_node(1) == 'b', "Incorrect output"
print("PASSED")

print("Asserting method 'get_node'")
assert linked_list.get_node(2) == 'e', "Incorrect output"
print("PASSED")

print("Asserting method 'get_node'")
assert linked_list.get_node(3) == 'f', "Incorrect output"
print("PASSED")
'''

linked_list = LinkedList('a')
linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.append('e')
linked_list.length()

print("Asserting method 'length'")
assert linked_list.length() == 5, "Incorrect output"
print("PASSED")

print("Printing linked_list")
linked_list.print_data()

print("Asserting method 'get_node'")
assert linked_list.get_node(2) == 'c', "Incorrect output"
print("PASSED")


linked_list.delete(2)
print("Asserting method 'length' after deleting a node")
assert linked_list.length() == 4, "Incorrect output"
print("PASSED")


linked_list.get_node(2)

print("Asserting method 'get_node'")
assert linked_list.get_node(2) == 'd', "Incorrect output"
print("PASSED")

print("Printing linked_list")
linked_list.print_data()

linked_list.insert('f', 2)

print("Asserting method 'length' after inserting a node")
assert linked_list.length() == 5, "Incorrect output"
print("PASSED")

print("Asserting method 'get_node'")
assert linked_list.get_node(2) == 'f', "Incorrect output"
print("PASSED")

print("Printing linked_list")
linked_list.print_data()
