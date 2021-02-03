def count_compression(string):
    tuple_list = []
    current_term = string[0]
    counter = 0

    for element in range(1, len(string) + 1):
        if element < len(string) and string[element] == current_term:
            counter += 1

        else:
            counter += 1
            tuple_list.append((current_term, counter))
            counter = 0

            if element < len(string):
                current_term = string[element]

    return tuple_list


def count_decompression(compressed_string):
    decompressed_string = ""

    for element in compressed_string:
        for num in range(element[1]):
            decompressed_string += str(element[0])

    return decompressed_string


print("Asserting count_compression on input [('a', 3), ('b', 2), ('c', 1), ('a', 4)]")
assert count_compression('aaabbcaaaa') == [('a', 3), ('b', 2), ('c', 1), ('a', 4)], "Incorrect output"
print("PASSED")

print("Asserting count_compression on input [('2', 2), ('3', 1), ('4', 5)]")
assert count_compression('22344444') == [('2', 2), ('3', 1), ('4', 5)], "Incorrect output"
print("PASSED")

print("Asserting count_decompression on input [('a', 3), ('b', 2), ('c', 1), ('a', 4)]")
assert count_decompression([('a', 3), ('b', 2), ('c', 1), ('a', 4)]) == "aaabbcaaaa", "Incorrect output"
print("PASSED")

print("Asserting count_decompression on input [(2,2), (3,1), (4,5)]")
assert count_decompression([(2, 2), (3, 1), (4, 5)]) == "22344444", "Incorrect output"
print("PASSED")
