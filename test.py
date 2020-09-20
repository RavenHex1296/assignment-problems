def less_than_4_letters(string):

    return [word for word in string.split(' ') if len(word) < 4]
print(less_than_4_letters("Hi FFFFFFF"))