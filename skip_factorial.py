def skip_factorial_nonrecursive(n):
    product = 1
    for element in range(n, 0, -2):
        product *= i

    return product


def skip_factorial_recursive(n):
    if n <= 2:
        if n % 2 == 0:
            return 2
        else:
            return 1

    return n * skip_factorial_recursive(n-2)

print("Asserting skip_factorial_nonrecursive on input '6'")
assert skip_factorial_nonrecursive(6) == 48
print("PASSED")

print("Asserting skip_factorial_nonrecursive on input '7'")
assert skip_factorial_nonrecursive(7) == 105
print("PASSED")

print("Asserting skip_factorial_recursive on input '6'")
assert skip_factorial_recursive(6) == 48
print("PASSED")

print("Asserting skip_factorial_recursive on input '7'")
assert skip_factorial_recursive(7) == 105
print("PASSED")
