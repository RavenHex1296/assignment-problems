def flatten(nested_dict):
    flattened_dict = {}
    for category in nested_dict:
        for key in nested_dict[category]:
            flattened_dict[category + "_" + key] = nested_dict[category][key]

    return flattened_dict

colors = {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}

print(flatten(colors))

print("Asserting flatten on input 'colors'")
assert flatten(colors) == {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}, "Nested_dict was flattened incorrectly"
print("PASSED")
