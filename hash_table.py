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
            return element[0]

print(array)
array = [[], [], [], [], []]

insert(array, 'a', [0,1])
insert(array, 'b', 'abcd')
insert(array, 'c', 3.14)
print(array)

insert(array, 'd', 0)
insert(array, 'e', 0)
insert(array, 'f', 0)
print(array)
