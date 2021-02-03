import random


def random_draw(distribution):
    cumulative_distribution = distribution

    for n in range(1, len(distribution)):
        cumulative_distribution[n] += cumulative_distribution[n - 1]

    for n in cumulative_distribution:
        if random_n > n:
            continue

        else:
            return cumulative_distribution.index(n)


print("True expect value of [0.5, 0.5] is 0.5. The average of the 1000 random samples is ")
sum = 0
for _ in range(1000):
    random_n = random.random()
    sum += random_draw([0.5, 0.5])
print(sum/1000)

print("True expect value of [0.25, 0.25, 0.5] is 1.25. The average of the 1000 random samples is ")
sum2 = 0
for _ in range(1000):
    random_n = random.random()
    sum2 += random_draw([0.25, 0.25, 0.5])
print(sum2/1000)

print("True expect value of [0.05, 0.2, 0.15, 0.3, 0.1, 0.2] is 2.8. The average of the 1000 random samples is ")
sum3 = 0
for _ in range(1000):
    random_n = random.random()
    sum3 += random_draw([0.05, 0.2, 0.15, 0.3, 0.1, 0.2])
print(sum3/1000)
