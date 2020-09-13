def identity_matrix_elements(n):
    return [[1 if j == i else 0 for j in range(n)] for i in range(n)]


def counting_across_rows_matrix_elements(m, n):
    return [[i * n + (j + 1) for j in range(n)] for i in range(m)]


print("Asserting identity_matrix_elements on input [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]")
assert identity_matrix_elements(4) == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], "Incorrect output"
print("PASSED")

print("Asserting counting_across_rows_matrix_elements on input (3, 4)")
assert counting_across_rows_matrix_elements(3, 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], "Incorrect output"
print("PASSED")
