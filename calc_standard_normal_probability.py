import math


def f(x):
    return math.exp((- x ** 2)/2) / ((2 * math.pi) ** 0.5)


def calc_standard_normal_probability(a, b):
    riemann_sum = 0
    current_point = a

    while current_point <= b:
        riemann_sum += 0.1 * f(current_point)
        current_point += 0.1

    return riemann_sum

print(calc_standard_normal_probability(-1, 1))
print(calc_standard_normal_probability(-2, 2))
print(calc_standard_normal_probability(-3, 3))
