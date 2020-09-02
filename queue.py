class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)
    
    def peek(self):
        return self.data[0]

q = Queue()

print("Asserting q.data")
assert q.data == [], "Incorrect output"
print("PASSED")

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print("Asserting q.enqueue()")
assert q.data == ["a", "b", "c"], "Incorrect output"
print("PASSED")

q.dequeue()
print("Asserting q.dequeue()")
assert q.data == ["b", "c"], "Incorrect output"
print("PASSED")

q.peek()
print("Asserting q.peek()")
assert q.peek() == "b", "Incorrect output"
print("PASSED")

print("Asserting q.data")
assert q.data == ["b", "c"]
print("PASSED")
