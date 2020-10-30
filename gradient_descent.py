def f(x, y):
    return 1 + x ** 2 + y ** 2


def f2(x, y):
    return 1 + x ** 2 + 2 * x + y ** 2 + 9 * y


def gradient_descent(f, initial_point, alpha, delta, iterations):
    x_guess = initial_point[0]
    y_guess = initial_point[1]

    for n in range(iterations):
        partial_dx = (f(x_guess + 0.5 * delta, y_guess) - f(x_guess - 0.5 * delta, y_guess)) / delta
        partial_dy = (f(x_guess, y_guess + 0.5 * delta) - f(x_guess, y_guess - 0.5 * delta)) / delta
        x_guess -= alpha * partial_dx
        y_guess -= alpha * partial_dy

    return round(f(x_guess, y_guess), 6)


#Part a: Minimum value is 1 for 1 + x ** 2 + y ** 2
print("Asserting gradient_descent for function 1 + x ** 2 + y ** 2")
assert gradient_descent(f, (1, 2), 0.01, 0.0001, 10000) == 1, "Incorrect output"
print("PASSED")

#Part c:
# 0 = 1 + x^2 + 2x + y^2 - 9y
# 0 = (x + 1)^2 + (y - 4.5) - 4.5^2
# The minimum of about -20.25 (which is -4.5^2) occurs at (-1, 4.5)
print("Asserting gradient_descent for function 1 + x^2 + 2x + y^2 - 9y")
assert gradient_descent(f2, (0, 0), 0.01, 0.0001, 10000) == -20.25, "Incorrect output"
print("PASSED")
