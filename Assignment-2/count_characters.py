def count_characters(input_string):
    final_dictionary = {}
    lowercase = input_string.lower()

    for character in lowercase:
        final_dictionary[character] = lowercase.count(character)

    return final_dictionary

print("Asserting count_characters works on input 'A cat!!!'")
assert count_characters("A cat!!!") == {'a': 2, ' ': 1, 'c': 1, 't': 1, '!': 3}, "Incorrect dictionary as the output"
print("PASSED")
