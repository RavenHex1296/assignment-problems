def even_odd_tuples(numbers):
    return [(i, "even") if i % 2 == 0 else (i, "odd") for i in numbers]

print("Asserting even_odd_tuples in operation on input [1,2,3,5,8,11]")
assert even_odd_tuples([1, 2, 3, 5, 8, 11]) == [(1, 'odd'), (2, 'even'), (3, 'odd'), (5, 'odd'), (8, 'even'), (11, 'odd')], "Incorrect output"
print("PASSED")


def even_odd_dict(numbers):
    return {key: ("even" if key % 2 == 0 else "odd") for key in numbers}

print("Asserting even_odd_dict is operational on input [1, 2, 3, 5, 8, 11]")
assert even_odd_dict([1, 2, 3, 5, 8, 11]) == {
    1:'odd',
    2:'even',
    3:'odd',
    5:'odd',
    8:'even',
    11:'odd'
}, "Incorrect output"
print("PASSED")
