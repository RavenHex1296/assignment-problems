from random import random

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


def probability(num_heads, num_flips):
    total_possibilities = 2 ** num_flips
    
    desired_outcomes = factorial(num_flips) / (
        factorial(num_heads) * factorial(num_flips - num_heads))

    return round((desired_outcomes / total_possibilities), 5)


def monte_carlo_probability(num_heads, num_flips):
    favored_outcomes = 0

    for time in range(1000):
        heads = 0

        for flip in range(num_flips):
            heads += round(random())

        if heads == num_heads:
            favored_outcomes += 1

    return favored_outcomes/1000


print("Asserting that probability works on input (5,8)")
assert probability(5, 8) == 0.21875, "Incorrect output"
print("PASSED")

for n in range(5):
  print("monte_carlo_probability", monte_carlo_probability(5,8))