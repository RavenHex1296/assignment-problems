import math


def f(x):
    return x ** 2 + 2 * x + 1


def f2(x):
    return (x ** 2 + math.cos(x)) / math.exp(math.sin(x))


def gradient_descent(f, x0, alpha, delta, iterations):
    updated_guess = x0

    for n in range(iterations):
        derivative = ((f(updated_guess + 0.5 * delta) - f(updated_guess - 0.5 * delta)) / delta)
        updated_guess -= alpha * derivative

    return f(updated_guess)


print("Estimated minimum value for x^2+2x+1: " + str(gradient_descent(f, 0, 0.01, 0.0001, 10000)))

print("Estimated minimum value for (x^2+cos(x))/(e^sin(x)): " + str(gradient_descent(f2, 0, 0.01, 0.0001, 10000)))
