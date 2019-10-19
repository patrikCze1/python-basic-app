from os import listdir
import os
p = str(input())

def getCurrentDir():
    print(os.getcwd())
    return str(os.getcwd())
#p = getCurrentDir()

def generateString(count, separator):
    string = ''
    for i in range(0, count):
        string += separator

    return string


def generateTree(path):
    depth = path.split('/')
    depth = len(depth) - 1
    print(path)
    for root, dirs, files in os.walk(path):
        for d in dirs:
            dirDepth = os.path.join(root, d)
            dirDepth = len(dirDepth.split('/'))
            
            string = generateString(dirDepth - depth, '-')
            print(string + d)
            string = generateString(dirDepth - depth, ' ')
            string += '|'
            for f in files:
                print(string + ' - ' + f)


generateTree(p)