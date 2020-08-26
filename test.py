def first_n_terms(n):
  terms = []
  curr_term = 5
  for i in range(n):
    terms.append(curr_term)
    curr_term = 3*curr_term - 4
  return terms


def nth_term(n):
  if n == 1:
    return 5
  return 3*nth_term(n-1) - 4

print("testing first_n_terms on input 10...")
assert first_n_terms(10) == [5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051], "first_n_terms(10) should equal [5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051]"
print("PASSED")

print("testing nth_term on input 10...")
assert nth_term(10) == 59051, "nth_term(10) should equal 59051"
print("PASSED")

  
def count_characters(input_string):
  lowercase_str = list(input_string.lower())
  return {char: lowercase_str.count(char) for char in lowercase_str}

print("testing count_characters on input 'A cat!!!'...")
assert count_characters('A cat!!!') == {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}, "count_characters('A cat!!!') should equal {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}"
print("PASSED")


def intersection(list_1, list_2):
  intersection_list = list(set(list_1) & set(list_2))
  intersection_nums = sorted([i for i in intersection_list if type(i) is int])
  intersection_strs = sorted([i for i in intersection_list if type(i) is str])

  return intersection_nums + intersection_strs


def union(list_1, list_2):
  union_list = list(set(list_1) | set(list_2))
  union_nums = sorted([i for i in union_list if type(i) is int])
  union_strs = sorted([i for i in union_list if type(i) is str])

  return union_nums + union_strs

print("testing intersection on inputs [1, 2, 'a', 'b'], [2, 3, 'a']...")
assert intersection([1, 2, 'a', 'b'], [2, 3, 'a']) == [2, 'a'], "intersection([1,2,'a','b'], [2,3,'a']) should equal [2, 'a']"
print("PASSED")

print("testing union on inputs [1,2,'a','b'], [2,3,'a']...")
assert union([1, 2, 'a', 'b'], [2, 3, 'a']) == [1, 2, 3, 'a', 'b'], "union([1,2,'a','b'], [2,3,'a']) should equal [1, 2, 3, 'a', 'b']"
print("PASSED")