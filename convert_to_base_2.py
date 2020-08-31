def convert_to_base_2(base_1_input):
    binaryNum = [0] * base_1_input
    index = 0
    string = ""

    while (base_1_input > 0):

        binaryNum[index] = base_1_input % 2
        base_1_input = int(base_1_input / 2)
        index += 1

    for string_index in range(index - 1, -1, -1):
        string += str(binaryNum[string_index])

    return string

print("Asserting convert_to_base_2 on input '19'")
assert convert_to_base_2(19) == "10011", "Incorrect conversion"
print("PASSED")
