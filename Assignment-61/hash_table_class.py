class HashTable:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = []

        for n in range(1, num_buckets + 1):
            self.buckets.append([])

    def hash_function(self, input_string):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        sum = 0

        for element in input_string:
            sum += alphabet.index(element)

        return sum % self.num_buckets

    def insert(self, key, value):
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].append((key, value))

    def find(self, key):
        bucket_index = self.hash_function(key)
        for element in self.buckets[bucket_index]:
            if element[0] == key:
                return element[1]


print("Asserting HashTable class")
ht = HashTable(num_buckets=3)
assert ht.buckets == [[], [], []]
assert ht.hash_function('cabbage') == 2

ht.insert('cabbage', 5)
assert ht.buckets == [[], [], [('cabbage', 5)]]

ht.insert('cab', 20)
assert ht.buckets == [[('cab', 20)], [], [('cabbage', 5)]]

ht.insert('c', 17)
assert ht.buckets == [[('cab', 20)], [], [('cabbage', 5), ('c', 17)]]

ht.insert('ac', 21)
assert ht.buckets == [[('cab', 20)], [], [('cabbage', 5), ('c', 17), ('ac', 21)]]

assert ht.find('cabbage') == 5
assert ht.find('cab') == 20
assert ht.find('c') == 17
assert ht.find('ac') == 21

print("PASSED")
