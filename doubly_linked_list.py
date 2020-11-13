class Node:
    def __init__(self, prev, data, next):
        self.prev = prev
        self.data = data
        self.next = next
        self.index = 0


class DoublyLinkedList:
    def __init__(self, head):
        self.head = Node(None, head, None)

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

    def append(self, next_node):
        current_node = self.head
        index = 0

        while current_node.next != None:
            current_node = current_node.next
            index += 1

        current_node.next = Node(current_node, next_node, None)
        current_node.next.index = index + 1

    def push(self, new_data):
        former_head = self.head
        self.head = Node(None, new_data, None)

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
        current_node = self.head

        for _ in range(index):
            current_node = current_node.next

        return current_node

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


doubly_linked_list = DoublyLinkedList('a')
doubly_linked_list.append('c')
doubly_linked_list.append('d')
doubly_linked_list.append('e')
doubly_linked_list.insert('b', 1)
doubly_linked_list.delete(3)
current_node = doubly_linked_list.get_node(3)
node_values = [current_node.data]
for _ in range(3):
    current_node = current_node.prev
    node_values.append(current_node.data)

print("Asserting methods 'append', 'delete', and 'get_node' work along with attribute 'prev'")
assert node_values == ['e', 'c', 'b', 'a'], "Incorrect output"
print("PASSED")
