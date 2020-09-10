def simple_sort(num_list):
    sorted_list = []

    while len(num_list) > 0:
        min_value = num_list[0]

        for element in num_list:

            if element < min_value:

                min_value = element

        sorted_list.append(min_value)
        num_list.remove(min_value)

    return sorted_list


def swap_sort(num_list):
    swap_count = 0

    for element in range(0, len(num_list)):
        if element + 1 < len(num_list) and num_list[element] > num_list[element +1 ]:
            temp = num_list[element + 1]
            num_list[element + 1] = num_list[element]
            num_list[element] = temp
            swap_count += 1

    if swap_count == 0:
        return num_list 

    return swap_sort(num_list)


print("Asserting simple_sort on input [5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]")
assert simple_sort([5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]) == [-5, 0, 2, 2, 2, 2, 3, 3.14, 4, 5, 8]
print("PASSED")

print("Asserting swap_sort on input [5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]")
assert swap_sort([5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]) == [-5, 0, 2, 2, 2, 2, 3, 3.14, 4, 5, 8]
print("PASSED")
