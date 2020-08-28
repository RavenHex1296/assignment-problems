class Stack:
    def __init__(self):
        self.data = []

    def push(self, new_data):
        self.data.append(new_data)

    def pop(self):
       return self.data.pop()

    def peek(self):
        return self.data[len(self.data)-1]

s = Stack()

print("Asserting s.data")
assert s.data == [], "Incorrect output"
print('PASSED')

s.push('a')
s.push('b')
s.push('c')

print("Asserting s.push")
assert s.data == ['a', 'b', 'c'], "Incorrect output"
print('PASSED')

s.pop()

print("Asserting s.pop")
assert s.data == ['a', 'b'], "Incorrect output"
print('PASSED')

print("Asserting s.peek")
assert s.peek() == 'b', "Incorrect output"
print('PASSED')

print("testing s.data...")
assert s.data == ['a', 'b'], "Incorrect output"
print('PASSED')
