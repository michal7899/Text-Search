import os, re

def search(regex, txt):
    searchRegex = re.compile(regex, re.I)
    result = searchRegex.findall(txt)

    print(result)

currentDir = os.getcwd()
print('Current working directory is: ' + currentDir)

dirAns = input('Is this the desired working directory, yes or no?')

if dirAns == 'yes':
    pass
elif dirAns == 'no':
    newDir = input('Please define working directory')
    currentDir = os.chdir(newDir)
    print('New current working directory is now: ' + newDir)

#testcwd = os.getcwd()
#print(testcwd)

folder = os.listdir(currentDir)

userRegex = input('What would you like to search for?')

for file in folder:
    if file.endswith('.txt'):
        txtfile = open(os.path.join(currentDir, file), 'r')
        msg = txtfile.read()
        search(userRegex, msg)
        # Add a count as to how many matches occur, either to search() or this loop









