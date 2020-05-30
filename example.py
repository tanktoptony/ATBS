import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me at 415-555-1011 tomorrow, or at 415-555-9999')
print(mo.group())

print(phoneNumRegex.findall('Call me at 415-555-1011 tomorrow, or at 415-555-9999'))

