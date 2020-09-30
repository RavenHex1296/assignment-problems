def insert_element_into_sorted_list(element, sorted_list):
    for num in range(len(sorted_list)):
        if sorted_list[num] >= element:
            return sorted_list[:num] + [element] + sorted_list[num:]

    return sorted_list + [element]


def card_sort(num_list):
    sorted_list = [num_list[0]]

    for num in range(1, len(num_list)):
        sorted_list = insert_element_into_sorted_list(num_list[num], sorted_list)

    return sorted_list

print("Asserting card_sort on input [12, 11, 13, 5, 6]")
assert card_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13], "Incorrect output"
print("PASSED")

print("Asserting card_sort on input [5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]")
assert card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]) == [-3, -3, -1, -1, -1, 1, 1, 3, 3, 5, 5, 7], "Incorrect output"
print("PASSED")
