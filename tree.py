def get_children(node, tree):
    children = []

    for branch in tree:
        if branch[0] == node:
            children.append(branch[1])

    return children


def get_parents(node, tree):
    parents = []

    for branch in tree:
        if branch[1] == node:
            parents.append(branch[0])

    return parents


def get_root(tree):
    for branch in tree:
        if get_parents(branch[0], tree) == []:
            return list(branch[0])


tree = [('a', 'c'), ('e', 'g'), ('e', 'i'), ('e', 'a'), ('d', 'b'), ('a', 'd'), ('d', 'f'), ('f', 'h'), ('d', 'j'), ('d', 'k')]

print("Asserting get_children on inpute 'e'")
assert get_children('e', tree) == ['g', 'i', 'a'], "Incorrect output"
print("PASSED")

print("Asserting get_children on inpute 'c'")
assert get_children('c', tree) == [], "Incorrect output"
print("PASSED")

print("Asserting get_children on inpute 'f'")
assert get_children('f', tree) == ['h'], "Incorrect output"
print('PASSED')

print("Asserting get_parents on inpute 'e'")
assert get_parents('e', tree) == [], "Incorrect output"
print("PASSED")

print("Asserting get_parents on inpute 'c'")
assert get_parents('c', tree) == ['a'], "Incorrect output"
print("PASSED")

print("Asserting get_parents on inpute 'f'")
assert get_parents('f', tree) == ['d'], "Incorrect output"
print('PASSED')

print("Asserting get_root")
assert get_root(tree) == ['e'], "Incorrect output"
print('PASSED')
