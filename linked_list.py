class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


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

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = Node(new_data, None)

    def push(self, new_data):
        new_node = Node(new_data) 

        new_node.next = self.head 

        self.head = new_node 

    def index(self,item):
        current = self.head

        while current != None:
            if current.data == item:
                return current.position

            else:
                current = current.next

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

''''
print("Asserting method 'index' for LinkedList")
assert linked_list.head.index == 0, "Incorrect output"
print("PASSED")
'''