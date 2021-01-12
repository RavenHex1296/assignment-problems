import math
import matplotlib.pyplot as plt


def f(x):
    return math.exp((- x ** 2)/2) / ((2 * math.pi) ** 0.5)


def calc_standard_normal_probability(a, b, n, rule):
    riemann_sum = 0
    step_size = (b - a) / n
    steps = []

    if rule == "Left endpoint rule":
        for num in range(0, n):
            steps.append(a + num * step_size)

        for num in steps:
            riemann_sum += step_size * f(num)

        return riemann_sum

    elif rule == "Right endpoint rule":
        for num in range(1, n + 1):
            steps.append(a + num * step_size)

        for num in steps:
            riemann_sum += step_size * f(num)

        return riemann_sum

    elif rule == "Midpoint rule":
        for num in range(0, n):
            steps.append(a + num * step_size)

        for num in steps:
            riemann_sum += step_size * f((num + num + step_size) / 2)

        return riemann_sum

    elif rule == "Trapezoidal rule":
        for num in range(1, n):
            steps.append(a + num * step_size)

        for num in steps:
                riemann_sum += f(num) * step_size

        return riemann_sum + 0.5 * step_size * f(a) + 0.5 * step_size * f(b)

    elif rule == "Simpson's rule":
        for num in range(1, n):
            steps.append(a + num * step_size)

        for num in steps:
            if steps.index(num) % 2 == 0:
                riemann_sum += 4 * (step_size / 3) * f(num)

            elif steps.index(num) % 2 == 1:
                riemann_sum += 2 * (step_size / 3) * f(num)

        return riemann_sum + (step_size / 3) * f(a) + (step_size / 3) * f(b)

left_riemann_sums = []
right_riemann_sums = []
midpoint_riemann_sums = []
trapezoidal_riemann_sums = []
simpson_riemann_sums = []

for num in range(2, 101, 2):
    left_riemann_sums.append(calc_standard_normal_probability(0, 1, num, "Left endpoint rule"))
    right_riemann_sums.append(calc_standard_normal_probability(0, 1, num, "Right endpoint rule"))
    midpoint_riemann_sums.append(calc_standard_normal_probability(0, 1, num, "Midpoint rule"))
    trapezoidal_riemann_sums.append(calc_standard_normal_probability(0, 1, num, "Trapezoidal rule"))
    simpson_riemann_sums.append(calc_standard_normal_probability(0, 1, num, "Simpson's rule"))

plt.style.use('bmh')
plt.plot([num for num in range(2, 101, 2)], left_riemann_sums, label="Left riemann sum")
plt.plot([num for num in range(2, 101, 2)], right_riemann_sums, label="Right riemann sum")
plt.plot([num for num in range(2, 101, 2)], midpoint_riemann_sums, label="Midpoint riemann sum")
plt.plot([num for num in range(2, 101, 2)], trapezoidal_riemann_sums, label="Trapezoidal riemann sum")
plt.plot([num for num in range(2, 101, 2)], simpson_riemann_sums, label="Simpson riemann sum")

plt.xlabel("Subintervals")
plt.ylabel("Estimated P(0<=x<=1)")
plt.legend(loc="upper right")
plt.savefig('calc_standard_normal_probability.png')
