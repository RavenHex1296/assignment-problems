from random import random
import matplotlib.pyplot as plt


def factorial(n):
    if n <= 1:
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


x_coords = [n for n in range(9)]
true_probability_distribution = [probability(n, 8) for n in x_coords]

plt.style.use('bmh')
plt.plot(x_coords, true_probability_distribution, linewidth=2.5)
plt.plot(x_coords, [monte_carlo_probability(n, 8) for n in x_coords], linewidth=0.75)
plt.plot(x_coords, [monte_carlo_probability(n, 8) for n in x_coords], linewidth=0.75)
plt.plot(x_coords, [monte_carlo_probability(n, 8) for n in x_coords], linewidth=0.75)
plt.plot(x_coords, [monte_carlo_probability(n, 8) for n in x_coords], linewidth=0.75)
plt.plot(x_coords, [monte_carlo_probability(n, 8) for n in x_coords], linewidth=0.75)
plt.legend(['True', 'MC 1', 'MC 2', 'MC 3', 'MC 4', 'MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 8 Coin Flips')
plt.savefig('coinflip.png')
