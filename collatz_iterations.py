import matplotlib.pyplot as plt


def collatz_iterations(number):
    iterations = []
    iterations.append(number)

    for n in iterations:
        if n % 2 == 0:
            iterations.append(n / 2)

        else:
            iterations.append(3 * n + 1)

        if n == 1:
            break

    return iterations.index(1)


def max_iterations():
    max_num = collatz_iterations(1)

    for num in range(1, 1001):
            if collatz_iterations(num) > max_num:
                max_num = collatz_iterations(num)

    return max_num

print("Asserting collatz_iterations on input 13")
assert collatz_iterations(13) == 9, "Incorrect output"
print("PASSED")

print(str(max_iterations()) + " has the highest number of Collatz iterations")

plt.style.use('bmh')
x_coords = range(1, 1001)
y_coords = [collatz_iterations(n) for n in range(1, 1001)]
plt.plot(x_coords, y_coords)
plt.xlabel('Numbers 1-1000')
plt.ylabel('Number of Collatz iterations')
plt.title('Number of Collatz iterations for numbers 1-1000')
plt.savefig('plot.png')
