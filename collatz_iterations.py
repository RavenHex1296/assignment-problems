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


def most_iterations():
    highest_number_of_iterations = collatz_iterations(1)
    number_with_most_iterations = 1

    for num in range(1, 1001):
        if collatz_iterations(num) > highest_number_of_iterations:
            highest_number_of_iterations = collatz_iterations(num)
            number_with_most_iterations = num

    return number_with_most_iterations

print("Asserting collatz_iterations on input 13")
assert collatz_iterations(13) == 9, "Incorrect output"
print("PASSED")

print(str(most_iterations()) + " has the highest number of Collatz iterations")

plt.style.use('bmh')
x_coords = range(1, 1001)
y_coords = [collatz_iterations(n) for n in range(1, 1001)]
plt.plot(x_coords, y_coords)
plt.xlabel('Numbers 1-1000')
plt.ylabel('Number of Collatz iterations')
plt.title('Number of Collatz iterations for numbers 1-1000')
plt.savefig('plot.png')
