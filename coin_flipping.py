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
    for number in range(5):
        success = 0

        for num in range(1000):
            results_of_flip_list = []

            for element in range(num_flips):
                results_of_flip = round(random())

                if results_of_flip == 0:
                    results_of_flip_list.append("H")

                else:
                    results_of_flip_list.append("T")

            if results_of_flip_list.count("H") == num_heads:
                success += 1

        print(success/1000)

print("Asserting that probability works on input (5,8)")
assert probability(5, 8) == 0.21875, "Incorrect output"
print("PASSED")

print("Monte Carlo probabilities for 5 heads out of 8 flips")
monte_carlo_probability(5, 8)
