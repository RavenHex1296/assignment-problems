import math
from random import random


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def probability(num_heads, num_flips):
    total_possibilities = 2 ** num_flips

    desired_outcomes = factorial(num_flips) / (
        factorial(num_heads) * factorial(num_flips - num_heads))

    return round((desired_outcomes / total_possibilities), 5)


def monte_carlo_probability(num_heads, num_flips, num_trials):
    favored_outcomes = 0

    for time in range(num_trials):
        heads = 0

        for flip in range(num_flips):
            heads += round(random())

        if heads == num_heads:
            favored_outcomes += 1

    return favored_outcomes / num_trials


def kl_divergence(p, q):
    relative_entropy = 0

    for element in range(0, len(p)):
        if p[element] != 0 and q[element] != 0:
            relative_entropy += p[element] * math.log(p[element] / q[element])

    return round(relative_entropy, 11)


p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]

print("Asserting kl_divergence on inputs [0.2, 0.5, 0, 0.3] and [0.1, 0.8, 0.1, 0]")
assert kl_divergence(p, q) == -0.09637237851, "Incorrect output"
print("PASSED")


q = [probability(i, 8) for i in range(9)]

print("Computing KL Divergence for MC Simulations...")

p = [monte_carlo_probability(i, 8, 100) for i in range(9)]
print("100 samples --> KL Divergence =" + str(kl_divergence(p, q)))

p = [monte_carlo_probability(i, 8, 1000) for i in range(9)]
print("1000 samples --> KL Divergence = " + str(kl_divergence(p, q)))

p = [monte_carlo_probability(i, 8, 10000) for i in range(9)]
print("10000 samples --> KL Divergence = " + str(kl_divergence(p, q)))

# As the number of samples increases, the KL divergence approaches 0 because as the number of samples rises, the approximate probability gets closer and closer to the true distribution.
