def min(num_list):
    minimum = num_list[0]

    for n in num_list:
        if n < minimum:
            minimum = n

    return minimum


def max(num_list):
    maximum = num_list[0]

    for n in num_list:
        if n > maximum:
            maximum = n

    return maximum


def tally_sort(num_list):
    minimum = min(num_list)
    tallys = []
    sorted_list = []

    for n in range(len(num_list)):
        num_list[n] -= minimum

    for n in range(max(num_list) + 1):
        tallys.append(0)

    for num in num_list:
        tallys[num] += 1

    for n in range(len(tallys)):
        for element in range(tallys[n]):
            sorted_list.append(n)

    for n in range(len(sorted_list)):
        sorted_list[n] += minimum

    return sorted_list

print("Asserting tally_sort on input [2, 5, 2, 3, 8, 6, 3]")
assert tally_sort([2, 5, 2, 3, 8, 6, 3]) == [2, 2, 3, 3, 5, 6, 8]
print("PASSED")
