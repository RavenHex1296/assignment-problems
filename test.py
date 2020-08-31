letters = " abcdefghijklmnopqrstuvwxyz"


def decode(numbers):
    decoded_string = ""
    for element in numbers:
        decoded_string += letters[int((element - b) / a)]

    return decoded_string

print(decode([377,
              717,
              71,
              513,
              105,
              921,
              581,
              547,
              547,
              105,
              377,
              717,
              241,
              71,
              105,
              547,
              71,
              377,
              547,
              717,
              751,
              683,
              785,
              513,
              241,
              547,
              751]))
