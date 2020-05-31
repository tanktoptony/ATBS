import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(phoneRegex.search('My phone number is 415-555-1234.'))
print(phoneRegex.search('My phone number is 555-1234.'))

# escaping

regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? in regex syntax'))

regex = re.compile(r'(\+\*\?)+')
print(regex.search('I learned about +*?+*?+*?+*?+*?+*? in regex syntax'))

haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said "HaHaHa"'))

haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('He said "HaHaHaHaHaHa"'))

haRegex = re.compile(r'(Ha){,5}')
print(haRegex.search('He said "HaHaHaHaHaHa"'))

haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('He said "HaHaHaHaHaHaHaHaHaHaHaHa"'))

# greedy match
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))

# non greedy match
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1234567890'))

"""
? matches zero or one times
* matches zero or more times
+ matches one or more times
{} matches a specific number of times and can accept a minimum and max value
? after curly braces makes it do a nongreedy match
"""
