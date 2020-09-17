
def make_nested(input_dict):
    nested_dict = {}

    for key in input_dict:
        splitter = key.split("_")
        if splitter[0] not in nested_dict:
            nested_dict[splitter[0]] = {}
        nested_dict[splitter[0]][splitter[1]] = input_dict.get(key)
    return nested_dict

colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}

print(make_nested(colors))

print("Testing make_nested on the input_dict 'colors'")
assert make_nested(colors) == {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}, "Incorrect nest"
print("PASSED")
