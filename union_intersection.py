def intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))

print(intersection([1, 2, 'a', 'b'], [2, 3, 'a']))


def union(list_1, list_2):
    return list(set(list_1) | set(list_2))

print(union([1, 2, 'a', 'b'], [2, 3, 'a']))
