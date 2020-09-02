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
        inverse_output = (element - b) / a
        not_integer = not( inverse_output.is_integer() )
        
        if not_integer or inverse_output < 0 or inverse_output > 25:
            return False

    return decoded_string


print("Asserting encode is operational on input ('a cat', 2, 3)")
assert encode('a cat', 2, 3) == [5, 3, 9, 5, 43], "Encoded incorrectly"
print("PASSED")

print("Asserting decode is operational on input ([5, 3, 9, 5, 43], 2, 3)")
assert decode([5, 3, 9, 5, 43], 2, 3) == "a cat", "Decoded incorrectly"
print("PASSED")

print("Asserting decode is operational on input ([1, 3, 9, 5, 43], 2, 3)")
assert not decode([1, 3, 9, 5, 43], 2, 3), "Decoded incorrectly"
print("PASSED")

print("Asseting decode is operational on input ([5, 3, 9, 5, 44], 2, 3)")
assert not decode([5, 3, 9, 5, 44], 2, 3), "Decoded incorrectly"
print("PASSED")


# Part C
encoded_list = [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751]

for a in range(1, 101):
    for b in range(1, 101):
        try:
            if decode(encoded_list, a, b) != False:
                print(a, b, decode(encoded_list, a, b), sep = "\n")
        except:
            pass

# Encoded_list was encoded using a = 34 and b = 71
