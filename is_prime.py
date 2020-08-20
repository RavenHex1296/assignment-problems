def is_prime(n):
    assert n > 1, "Input too small"
    for divisor in range(2, n):
        if (n / divisor) % 1 == 0:
            return False
    return True

print(is_prime(59))
print("Testing is_prime on input 59")
assert is_prime(59), "59 is prime"
print("PASSED")


print(is_prime(51))
print("Testing is_prime on input 51")
assert not is_prime(51), "51 isn't prime"
print("PASSED")
