input_string = input('')
reverse_string = input_string[::-1]

def is_symmetric(input_string): 
  if reverse_string == input_string:
    print("True")
  else:
    print("False") 
is_symmetric('racecar')
is_symmetric('batman')

print('testing is_symmetric on the input {}'.format(input_string))
assert reverse_string == input_string, 'The input_string {} is not a palindrome'.format(input_string)
print('PASSED')