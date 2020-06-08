import re
namesRegex = re.compile(r'Agent \w+')


print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

# substitution method
print(namesRegex.sub('REDACTED',
                     'Agent Alice gave the secret documents to Agent Bob.'))

# Using \1 \2 \3 to sub groups 1 2 and 3 in the regex patterns

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub(r'Agent \1****',
                     'Agent Alice gave the secret documents to Agent Bob.'))

# Verbose mode re.VERBOSE

re.compile(r'''
(\d\d\d-) |   #area code (without parens, with dash)
(\(\d\d\d-) ) # -or- area code with parens and no dash
\d\d\d      # first 3 digits
-           # second dash
\d\d\d\d    # last 4 digits
\sx\d{2,4}  # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
