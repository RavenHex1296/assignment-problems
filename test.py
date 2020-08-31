letters = " abcdefghijklmnopqrstuvwxyz"


def decode(numbers, a, b):
    decoded_string = ""
    for element in numbers:
        decoded_string += letters[int((element - b) / a)]
        if ((element - b) / a).is_integer() == False or int((element - b) / a) < 0 or letters[int((element - b) / a)] == "z":
          return False
    return decoded_string
