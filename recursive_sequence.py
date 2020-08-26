def first_n_terms(n):
    assert n > 0, "Input must be positive"
    sequence = []

    for element in range(1, n):
        if element == 1:
            preceding_term = 5
            sequence.append(5)

        sequence.append(3 * preceding_term - 4)
        preceding_term = 3 * preceding_term - 4

    return sequence

print("Asserting first_n_terms on input 10")
assert first_n_terms(10) == [5, 11, 29, 83, 245, 731,
                             2189, 6563, 19685, 59051], "Incorrect output"
print("PASSED")


def nth_term(n):
    if n == 1:
        return 5
    return 3 * nth_term(n - 1) - 4


print("Asserting nth_term on input 10")
assert nth_term(10) == 59051, "Incorrect output"
print("PASSED")
