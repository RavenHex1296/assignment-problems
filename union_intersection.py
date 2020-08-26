def intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))

print("Asserting intersection on inputs [1, 2, 'a', 'b'], [2, 3, 'a']")
assert intersection([1, 2, 'a', 'b'], [2, 3,
                                       'a']) == [2,
                                                 'a'], "Incorrect intersection"
print("PASSED")


def union(list_1, list_2):
    return list(set(list_1) | set(list_2))

print("Asserting union on inputs [1,2,'a','b'], [2,3,'a']...")
assert union([1, 2, 'a', 'b'], [2, 3,
                                'a']) == [1,
                                          2, 3, 'a', 'b'], "Incorrect union"
print("PASSED")
