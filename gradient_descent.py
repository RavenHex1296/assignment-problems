import math


def f(x):
    return x ** 2 + 2 * x + 1


def gradient_descent(f, x0, alpha, delta, iterations=1000):
    guess = x0

    for n in range(iterations):
        derivative = ((f(guess + 0.5 * delta) - f(guess - 0.5 * delta)) / delta)
        guess -= alpha * derivative

    return round(f(guess), 6)

print("Estimated minimum value for x^2+2x+1: " + str(gradient_descent(f, 0, 0.01, 0.0001, 10000)))
def f(x):
    return (x**2 + math.cos(x)) / math.exp(math.sin(x))

print("Estimated minimum value for (x^2+cos(x))/(e^sin(x)): " + str(gradient_descent(f, 0, 0.01, 0.0001, 10000)))