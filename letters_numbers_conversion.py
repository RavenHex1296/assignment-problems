letters = [' ', 'a', 'b', 'c', 'd',
           'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x',
           'y', 'z']


def convert_to_numbers(input_string):
    input_numbers = list(input_string)
    converted_letters = []

    for letter in input_numbers:
        converted_letters.append(letters.index(letter))

    return converted_letters

print(convert_to_numbers("a cat"))
print("Testing convert_to_numbers for input 'a cat'")
assert convert_to_numbers("a caz") == [1, 0, 3, 1, 20], "Wrong conversion"
print("PASSED")


def convert_to_letters(input_string):
    converted_numbers = ""
    for number in input_string:
        converted_numbers += letters[number]

    return converted_numbers

print(convert_to_letters([1, 0, 3, 1, 20]))
print("Testing convert_to_letters for input [1, 0, 3, 1, 20]")
assert convert_to_letters([1, 0, 3, 1, 20]) == "a cat", "Wrong conversion"
print("PASSED")
