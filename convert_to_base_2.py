def convert_to_base_2(base_10_input):
    binary_number = [0] * base_1_input
    index = 0
    base_2_string = ""

    while (base_10_input > 0):

        binary_number[index] = base_1_input % 2
        base_10_input = int(base_1_input / 2)
        index += 1

    for string_index in range(index - 1, -1, -1):
        base_2_string += str(binary_number[string_index])

    return int(base_2_string)

print("Asserting convert_to_base_2 is operational on input '19'")
assert convert_to_base_2(19) == 10011, "Incorrect conversion"
print("PASSED")
