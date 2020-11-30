import matplotlib.pyplot as plt
import math


def f(x):
    return 1 / (1 + math.exp(-0.6931 * x + 2.2146))

x_coords = [0, 1, 2, 3]
y_coords = []

for num in x_coords:
    y_coords.append(f(num))

plt.style.use('bmh')
plt.plot(x_coords, y_coords)
plt.plot([1, 2, 3], [0.2, 0.25, 0.5], 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('logistic_regression.png')
