def zero_of_tangent_line(c):
    f_of_c = c ** 3 + c - 1
    m = 3 * c ** 2 + 1
    b = f_of_c - (c * m)
    x_intercept = (-1 * b) / m

    return round(x_intercept, 6)


def estimate_solution(init_guess, precision):
    estimate = zero_of_tangent_line(init_guess)
    previous_guess = zero_of_tangent_line(init_guess) + precision

    while abs(estimate - previous_guess) >= precision:
        previous_guess = estimate
        estimate = zero_of_tangent_line(estimate)

    return estimate

print("Asseting zero_of_tangent_line on input 0.5")
assert zero_of_tangent_line(0.5) == 0.714286
print("PASSED")

print("Asseting estimate_solution on input 0.5, 0.01")
assert estimate_solution(0.5, 0.01) == 0.682328
print("PASSED")
