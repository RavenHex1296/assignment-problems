def intersection(list_1, list_2):
    intersections = list(set(list_1) & set(list_2))
    return intersections

print(intersection([1, 2, 'a', 'b'], [2, 3, 'a']))


def union(list_1, list_2):
    union_list = list(set(list_1) | set(list_2))
    return union_list

print(union([1, 2, 'a', 'b'], [2, 3, 'a']))
