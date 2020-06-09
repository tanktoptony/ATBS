# Plaintext and Binary Files

helloFile = open('c:\\users\\antho\\desktop\\github\\git-repos\\ATBS\\hello.txt')

helloFile.read()
helloFile.close()

'''
>>> os.getcwd()
'C:\\Users\\antho\\Desktop\\GitHub\\git-repos\\ATBS'
>>> baconFile = open('bacon.txt', 'w')
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> baconFile = open('bacon.txt', 'a')
>>> baconFile.write('\n\nBacon is delicious.')
21
>>> baconFile.close()
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-Tail', 'Cleo']
>>> shelfFile.close()
>>> shelfFile = shelve.open('mydata')
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon', 'Fat-Tail', 'Cleo']
>>> shelfFile.close()
>>>
'''
