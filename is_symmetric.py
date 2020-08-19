def is_symmetric(input_string): 
  reverse = input_string[::-1]
  if reverse_string == input_string:
    print("True")
  else:
    print("False") 

is_symmetric('racecar')
is_symmetric('batman')

print('testing is_symmetric on input racecar and batman')
assert reverse_string == input_string, 'The input_string {} is not a palindrome'.format(input_string)
print('PASSED')