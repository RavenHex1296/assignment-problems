class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop([0])
    
    def peek(self):
        return self.data[0]

q = Queue()

print(q.data)

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q.data)

q.dequeue()
print(q.data)

q.peek()
print(q.data)
