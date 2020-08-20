letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def convert_to_letters(input_string):
    print('a')
    converted_numbers = ""
    for number in input_string:
        converted_numbers += letters[number]
    print('b')

    print(converted_numbers)
    return converted_numbers
    print('c')

convert_to_letters([1, 0, 3, 1, 20])

print("Testing convert_to_letters for input [1, 0, 3, 1, 20]")
assert convert_to_letters([1, 0, 3, 1, 20]) == "a cat", "Wrong conversion"
print("PASSED")