def merge(x, y):
    merged_list = []
    longer_list = x if len(x) > len(y) else y
    shorter_list = y if len(x) > len(y) else x
    long_list_index = 0

    for n in range(len(shorter_list)):
        while long_list_index < len(longer_list) and longer_list[long_list_index] < shorter_list[n]:
            merged_list.append(longer_list[long_list_index])
            long_list_index += 1

        merged_list.append(shorter_list[n])

    for n in range(long_list_index, len(longer_list)):
        merged_list.append(longer_list[n])

    return merged_list


def merge_sort(input_list):
    if len(input_list) < 2:
        return input_list

    left = input_list[:round(len(input_list)/2)]
    right = input_list[round(len(input_list)/2):]
    sorted_first_half = merge_sort(left)
    sorted_last_half = merge_sort(right)
    return merge(sorted_first_half, sorted_last_half)


print("Asserting merge_sort")
assert merge_sort([4, 8, 7, 7, 4, 2, 3, 1]) == [1, 2, 3, 4, 4, 7, 7, 8], "Incorrect output"
print("PASSED")

print(merge_sort([2, 1]))
