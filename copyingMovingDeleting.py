import shutil, os, send2trash
'''

# copy a file to a folder
shutil.copy('c:\\spam.txt', 'c:\\delicious')

# copy and rename a file to a new folder
shutil.copy('c:\\spam.txt', 'c:\\delicious\\spam2.txt')

# copy a directory and all files to a new folder
shutil.copy('c:\\delicious', 'c:\\delicious_backup')

# move a file removing it from origin
shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut')

# renaming a file
shutil.move('c:\\delicious\\spam.txt', 'c:\\delicious\\spam2.txt')


# deletion
os.unlink('bacon.txt')

# delete a whole directory
shutil.rmtree('c:\\delicious')
'''

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)

# send2trash module
# send2trash.send2trash('bacon.txt')

# walking a directory tree
for folderName, subfolders, filenames in os.walk('c:\\users\\antho\\desktop'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')
    
