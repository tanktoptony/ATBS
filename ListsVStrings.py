name = 'Sophie'
print(name[0])
print(name[1:3])

for letter in name:
    print(letter)

# mutable v immutable

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
print(cheese)
print(spam)
