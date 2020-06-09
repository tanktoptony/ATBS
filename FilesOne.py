import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
print(os.sep)

print(os.getcwd())
os.chdir('C:\\')
print(os.getcwd())

# relative file paths and absolute paths
''' absolute paths always begin with C or some other root folder'''

# os.chdir('C:\Users\antho\Desktop\GitHub\git-repos\ATBS')

print(os.path.isabs('C:\\Users\\antho\\Desktop\\GitHub\\git-repos\\ATBS\\FilesOne.py'))

print(os.path.relpath('C:\\Users\\antho\\Desktop\\GitHub\\git-repos\\ATBS', 'C:\\Users\\antho\\Desktop'))

# >>> os.path.exists('c:\\windows\\system32\\calc.exe')
# >>> os.path.isdir('c:\\windows\\system32')
# >>> os.path.isfile('c:\\windows\\system32\\calc.exe')

