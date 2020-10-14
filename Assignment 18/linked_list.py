class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.index = 0


class LinkedList:
    def __init__(self, head):
        self.head = Node(head, None)

    def print_data(self):
        current_node = self.head

        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next

        print(current_node.data)

    def length(self):
        current_node = self.head
        num_nodes = 1

        while current_node.next != None:
            num_nodes += 1
            current_node = current_node.next

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

''''
A = Node(4)
print("Asserting 'data' for class 'Node'")
assert A.data == 4, "Incorrect output"
print("PASSED")

print("Asserting method 'next' for class 'Node'")
assert A.next == None, "Incorrect output"
print("PASSED")

B = Node(8)
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
'''
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
