def f(x):
    return x ** 3 + x - 1


def estimate_derivative(f, c, delta):
    return (f(c + delta / 2) - f(c - delta / 2)) / delta


def zero_of_tangent_line(f, c, delta):
    x = c
    y = f(c)
    m = estimate_derivative(f, c, delta)
    b = y - (m * x)
    x_intercept = (-1 * b) / m
    return round(x_intercept, 6)


def estimate_solution(f, initial_guess, delta, precision):
    estimate = zero_of_tangent_line(f, initial_guess, delta)
    previous_guess = zero_of_tangent_line(f, initial_guess, delta) + precision

    while abs(estimate - previous_guess) >= precision:
        previous_guess = estimate
        estimate = zero_of_tangent_line(f, estimate, delta)

    return round(estimate, 6)


print("Asserting zero_of_tangent_line")
assert zero_of_tangent_line(f, 0.5, 0.001) == 0.714286, "Incorrect output"
print("PASSED")

print("Asserting estimate_solution")
assert estimate_solution(f, 0.5, 0.001, 0.01) == 0.682328, "Incorrect output"
print("PASSED")
