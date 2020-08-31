letters = " abcdefghijklmnopqrstuvwxyz"


def encode(string, a, b):
    encoded_string = []
    for element in string:
        encoded_string.append(a * letters.find(element) + b)

    return encoded_string


def decode(numbers, a, b):
    decoded_string = ""
    for element in numbers:
        decoded_string += letters[int((element - b) / a)]
    return decoded_string


print("Asserting encode is operational on input ('a cat', 2, 3)")
assert encode('a cat', 2, 3) == [5, 3, 9, 5, 43], "Encoded incorrectly"
print("PASSED")

print("Asserting decode is operational on input ([5, 3, 9, 5, 43], 2, 3)")
assert decode([5, 3, 9, 5, 43], 2, 3) == "a cat", "Decoded incorrectly"
print("PASSED")
