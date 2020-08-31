letters = " abcdefghijklmnopqrstuvwxyz"


def decode(numbers, a, b):
    decoded_string = ""
    for element in numbers:
        decoded_string += letters[int((element - b) / a)]
        if ((element - b) / a).is_integer() == False or int((element - b) / a) < 0 or int((element - b) / a) >25:
            return False
    return decoded_string

print(decode([5, 3, 9, 5, 44], 2, 3))
