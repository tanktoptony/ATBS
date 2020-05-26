listy = []*5


spam = ['cat', 'bat', 'rat', 'elephant']

#slicing using colons - up to but does not include

del spam[3] #deletes index 3 item

listHello = list('Hello')

isCat = 'cat' in spam

isEl = 'elephant' in spam

#practicing for loops with lists, multiple assignment and augmented operators
for i in [0, 1, 2, 3]:
    print(i)


listy2 = list(range(4))

for i in range(len(spam)):
    print('Index ' + str(i) + ' in supplies is: ' + spam[i])

goblin = ['green', 'bite attack', 25]

color = goblin[0]
attack = goblin[1]
HP = goblin[2]

print('The Goblin enemy has ' + color + ' skin, attacks with ' + attack + ' and has ' + str(HP) + ' hit points.')

# list methods

spam2 = ['hello', 'hi', 'howdy', 'heya']

spam2.index('heya')

# sort method happens in ASCII order, if you want to have normal alpha,
# pass the key = str.lower to the method
