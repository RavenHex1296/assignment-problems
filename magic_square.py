def diagonals(input_magic_square):
    diagonal = [[], []]

    for row in range(len(input_magic_square)):
        for column in range(len(input_magic_square[0])):
            if row == column:
                diagonal[0].append(input_magic_square[row][column])

    column_index = len(input_magic_square[0]) - 1

    for row in range(len(input_magic_square)):
        diagonal[1].append(input_magic_square[row][column_index])
        column_index -= 1

    return diagonal

def rows(input_magic_square):
    return input_magic_square

def columns(input_magic_square):
    columns = [[input_magic_square[row][column] for row in range(len(input_magic_square))] for column in range(len(input_magic_square[0]))]
    return columns


def is_valid(input_magic_square):
    for diagonal in diagonals(input_magic_square):
        if None in diagonal:
            continue

        elif sum(diagonal) != 15:
            return False

    for row in rows(input_magic_square):
        if None in row:
            continue

        elif sum(row) != 15:
            return False

    for column in columns(input_magic_square):
        if None in column:
            continue

        elif sum(column) != 15:
            return False

    return True

'''
arr1 = [[1,2,None],[None,3,None],[None,None,None]]
assert is_valid(arr1)

arr2 = [[1,2,None],[None,3,None],[None,None,4]] 
assert not is_valid(arr2)

arr3 = [[1,2,None],[None,3,None],[5,6,4]]
assert not is_valid(arr3)

arr4 = [[None, None, None],[None, 3, None], [5, 6, 4]] 
assert is_valid(arr4)
'''

def magic_square_elements(input_magic_square):
    elements = [input_magic_square[row][column] for column in range(len(input_magic_square[0])) for row in range(len(input_magic_square))]
    return elements


magic_square = [[None, None, None], [None, None, None], [None,  None,None]]
for num1 in range(1, 10):
    used_numbers = []
    if None not in magic_square_elements(magic_square) and is_valid(magic_square):
        break

    magic_square = [[num1, None, None], [None, None, None], [None, None, None]]
    used_numbers.append(num1)

    if not is_valid(magic_square):
        continue

    for num2 in range(1, 10):
        if None not in magic_square_elements(magic_square) and is_valid(magic_square):
            break

        if num2 not in [num1]:
            magic_square = [[num1, num2, None], [None, None, None], [None, None, None]]

        else:
            continue

        if not is_valid(magic_square):
            continue

        for num3 in range(1, 10):
            if None not in magic_square_elements(magic_square) and is_valid(magic_square):
                break

            if num3 not in [num1, num2]:
                magic_square = [[num1, num2, num3], [None, None, None], [None, None, None]]

            else:
                continue

            if not is_valid(magic_square):
                continue

            for num4 in range(1, 10):
                if None not in magic_square_elements(magic_square) and is_valid(magic_square):
                    break

                if num4 not in [num1, num2, num3]:
                    magic_square = [[num1, num2, num3], [num4, None, None], [None, None, None]]

                else:
                    continue

                if not is_valid(magic_square):
                    continue

                for num5 in range(1, 10):
                    if None not in magic_square_elements(magic_square) and is_valid(magic_square):
                        break

                    if num5 not in [num1, num2, num3, num4]:
                        magic_square = [[num1, num2, num3], [num4, num5, None], [None, None, None]]

                    else:
                        continue

                    if not is_valid(magic_square):
                        continue

                    for num6 in range(1, 10):
                        if None not in magic_square_elements(magic_square) and is_valid(magic_square):
                            break

                        if num6 not in [num1, num2, num3, num4, num5]:
                            magic_square = [[num1, num2, num3], [num4, num5, num6], [None, None, None]]

                        else:
                            continue

                        if not is_valid(magic_square):
                            continue

                        for num7 in range(1, 10):
                            if None not in magic_square_elements(magic_square) and is_valid(magic_square):
                                break

                            if num7 not in [num1, num2, num3, num4, num5, num6]:
                                magic_square = [[num1, num2, num3], [num4, num5, num6], [num7, None, None]]

                            else:
                                continue

                            if not is_valid(magic_square):
                                continue

                            for num8 in range(1, 10):
                                if None not in magic_square_elements(magic_square) and is_valid(magic_square):
                                    break

                                if num8 not in [num1, num2, num3, num4, num5, num6, num7]:
                                    magic_square = [[num1, num2, num3], [num4, num5, num6], [num7, num8, None]]

                                else:
                                    continue

                                if not is_valid(magic_square):
                                    continue

                                for num9 in range(1, 10):
                                    if None not in magic_square_elements(magic_square) and is_valid(magic_square):
                                        break

                                    if num9 not in [num1, num2, num3, num4, num5, num6, num7, num8]:
                                        magic_square = [[num1, num2, num3], [num4, num5, num6], [num7, num8, num9]]

                                    else:
                                        continue

                                    if not is_valid(magic_square):
                                        continue
print(magic_square)