array = [[], [], [], [], []] # has 5 empty "buckets"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def hash_function(string):
    sum = 0

    for element in string:
        sum += alphabet.index(element)

    return sum % 5


def insert(array, key, value):
    bucket_index = hash_function(key)
    array[bucket_index].append((key, value))


def find(array, key):
    bucket_index  = hash_function(key)
    for element in array[bucket_index]:
        if element[0] == key:
            return element[1]

print("Asserting hash_function, insert, and find")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(array, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(array, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value
print("PASSED")
