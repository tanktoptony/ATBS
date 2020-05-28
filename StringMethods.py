# String Methods
# pgs 128 - 141

spam = 'Hello'
print(spam.upper())
print(spam.lower())

print(spam.isupper())
print(spam.lower().islower())

spam.isalpha()
spam.isalnum()
spam.isdecimal()
spam.isspace()
print(spam.istitle())

# startswith()
# endswith()

# join method

print(', '.join(['cats', 'rats', 'bats']))
print('My name is Simon'.split())
print('My name is Simon'.split('m'))

print('Hello'.rjust(20, '*'))
print(spam.center(20))

# getting rid of white space characters with strip, lstrip and rstrip
print('       x '.lstrip())

# pyperclip module
