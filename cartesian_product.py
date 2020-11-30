def cartesian_product(arrays):
    points = [[]]

    for arr in arrays:
        for _ in range(len(points)):
            for element in arr:
                new_points = list(points[0])
                new_points.append(element)
                points.append(new_points)

            points.remove(points[0])

    return points

print("Asserting cartesian_product")
assert cartesian_product([['a'], [1, 2, 3], ['Y', 'Z']]) == [['a', 1, 'Y'], ['a', 1, 'Z'], ['a', 2, 'Y'], ['a', 2, 'Z'], ['a', 3, 'Y'], ['a', 3, 'Z']], "Incorrect output"
print("PASSED")
