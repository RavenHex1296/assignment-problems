def unlist_nonrecursive(x):
    while True:
        try:
            for element in x:
                if list(element) != element:
                    return x

            x = element

        except:
            if len(x) == 1:
                return x[0]

            else:
                return x


def unlist_recursive(x):
    try:
        for element in x:
            if list(element) != element:
                return x
        return unlist_recursive(element)

    except:
        if len(x) == 1:
            return x[0]

        else:
            return x


print("Asserting unlist_nonrecursive on input [[[[1], [2,3], 4]]]")
assert unlist_nonrecursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4], "Incorrect output"
print("PASSED")

print("Asserting unlist_nonrecursive on input [[[[1]]]]")
assert unlist_nonrecursive([[[[1]]]]) == 1, "Incorrect output"
print("PASSED")

print("Asserting unlist_recursive on input [[[[1], [2,3], 4]]]")
assert unlist_recursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4], "Incorrect output"
print("PASSED")

print("Asserting unlist_recursive on input [[[[1]]]]")
assert unlist_recursive([[[[1]]]]) == 1, "Incorrect output"
print("PASSED")
