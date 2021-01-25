test_string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'

strings = [x.split(',') for x in test_string.split('\n')]

converted_string = []

for string in strings:
    new_string = []

    if len(string) > 0:
        for element in string:
            if element[0]=='"' and element[-1]=='"':
                new_string.append(element[1:])

            elif '.' in element:
                new_string.append(float(element))

            else:
                new_string.append(int(element))

        converted_string.append(new_string)

print(converted_string)
