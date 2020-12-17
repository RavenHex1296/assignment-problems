def convert_to_base_10(input_binary_number):
    decimal = 0
    input_as_string = str(input_binary_number)
    exponent = len(str(input_binary_number)) - 1

    for digit in input_as_string:
        decimal += int(digit) * (2 ** exponent)
        exponent -= 1
    if exponent < 0:
        return decimal

print("Testing convert_to_base_10 on input '10011'")
assert convert_to_base_10(10011) == 19, "Incorrect output"
print("PASSED")
