def merge(x,y):
    merged_list = []
    longer_list = []
    shorter_list = []
    long_list_index = 0

    if len(x) > len(y):
        longer_list = x
        shorter_list = y

    elif len(x) < len(y):
        longer_list = y
        shorter_list = x

    for n in range(len(shorter_list)):
        while long_list_index < len(longer_list) and longer_list[long_list_index] < shorter_list[n]:
            merged_list.append(longer_list[long_list_index])
            long_list_index += 1 

        merged_list.append(shorter_list[n])

    for n in range(long_list_index, len(longer_list)):
        merged_list.append(longer_list[n])

    return merged_list

print("Asserting 'merge'")
assert merge([-2, 1, 4, 4, 4,5,7],[-1,6,6]) == [-2, -1, 1, 4, 4, 4, 5, 6, 6, 7]
print("PASSED")
