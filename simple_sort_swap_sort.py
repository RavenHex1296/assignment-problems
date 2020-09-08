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
    while min(num_list) != num_list[0]:

        for element in range(0, len(num_list) - 1):
            preceding_element = num_list[element]
            next_element = num_list[element + 1]

            if preceding_element > next_element:
                num_list[element] = next_element
                num_list[element + 1] = preceding_element

    return num_list


print("Asserting simple_sort on input [5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]")
assert simple_sort([5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]) == [-5, 0, 2, 2, 2, 2, 3, 3.14, 4, 5, 8]
print("PASSED")

print("Asserting swap_sort on input [5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]")
assert swap_sort([5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]) == [-5, 0, 2, 2, 2, 2, 3, 3.14, 4, 5, 8]
print("PASSED")
