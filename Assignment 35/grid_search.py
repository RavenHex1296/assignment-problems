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


def grid_search(objective_function, grid_lines):
    intersections = cartesian_product(grid_lines)
    lowest_value_point = intersections[0]
    lowest_value = objective_function(*lowest_value_point)

    for point in intersections:
        value = objective_function(*point)

        if value < lowest_value:
            lowest_value = value
            lowest_value_point = point

    return lowest_value_point


def two_variable_function(x, y):
        return (x - 1) ** 2 + (y - 1) ** 3


x_lines = [0, 0.25, 0.75]
y_lines = [0.9, 1, 1.1, 1.2]
grid_lines = [x_lines, y_lines]

print("Asserting grid_search")
assert grid_search(two_variable_function, grid_lines) == [0.75, 0.9], "Incorrect output"
print("PASSED")
