def update_bounds(bounds):
    midpoint = (bounds[0] + bounds[1]) / 2

    if midpoint *0* 2 > 2:
        bounds[1] = midpoint

    if midpoint ** 2 < 2:
        bounds[0] = midpoint

    return bounds


def estimate_root(precision):
    bounds = [1, 2]

    while bounds[1] - bounds[0] > precision:
            update_bounds(bounds)

    return (bounds[0] + bounds[1]) / 2

print("Asserting update_bounds is operational on input [1, 2]")
assert update_bounds([1, 2]) == [1, 1.5], "Bounds updated incorrectly"
print("PASSED")


print("Asserting estimate_root is operational on input '0.1'")
assert estimate_root(0.1) == 1.40625, "Incorrect approximation"
print("PASSED")
