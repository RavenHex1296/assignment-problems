def arr_to_square(arr):
    return [arr[n:n + 6] for n in range(0, len(arr), 6)]


def is_valid(arr):
    for row in arr:
        if None not in row:
            if sum(row) != 21:
                return False

        else:
            row = [n for n in row if n != None]

            if len(set(row)) != len(row):
                return False

    columns = []

    for column_index in range(len(arr)):
        column = []

        for row in arr:
            column.append(row[column_index])

        columns.append(column)

    for column in columns:
        if None not in column:
            if sum(column) != 21:
                return False

        else:
            column = [n for n in column if n != None]

            if len(set(column)) != len(column):
                return False

    upper_left_corners = [(0, 0), (0, 3), (2, 0), (2, 3), (4, 0), (4, 3)]

    for corner in upper_left_corners:
        group = []

        for row in range(0, 2):
            for column in range(0, 3):
                n = arr[row + corner[0]][column + corner[1]]

                if n in group:
                    return False

                if n != None:
                    group.append(n)

    return True


arr = [[None, None, 4, None, None, None], [None, None, None, 2, 3, None], [3, None, None, None, 6, None], [None, 6, None, None, None, 2], [None, 2, 1, None, None, None], [None, None, None, 5, None, None]]



def solve_sudoku(square):
    square = sum(square, [])
    known_entries = [n for n in range(len(square)) if square[n] != None]
    index = 0
    forward = True

    while None in square or not is_valid(arr_to_square(square)):
        if index in known_entries:
            if forward:
                index += 1 

            else:
                index -= 1
          
            continue

        if square[index] == None:
            square[index] = 0

        square[index] += 1

        if square[index] >= 7:
            square[index] = None
            index -= 1
            forward = False
            continue

        if is_valid(arr_to_square(square)):
            index += 1
            forward = True

    return arr_to_square(square)


square = solve_sudoku([[None, None, 4, None, None, None],
                           [None, None, None, 2, 3, None],
                           [3, None, None, None, 6, None],
                           [None, 6, None, None, None, 2],
                           [None, 2, 1, None, None, None],
                           [None, None, None, 5, None, None]])

print(" " + "-" * 16)

for n in square:
    print(n)

print(" " + "-" * 16)
