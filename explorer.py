import os
import sys
from os.path import exists


def main():
    print('Welcome to my file explorer terminal')
    commands = ['mkdir', 'exit', 'dir', 'pwd', 'commands', 'cd', 'rm',
                'mkfl']
    currDir = 'C:/Users'
    os.chdir(currDir)
    userInput = ''
    while (True):
        userInput = input().strip()
        try:
            userInput = userInput.split()
            userCommand = userInput[0]
            if userCommand == commands[0]:
                makeDir(' '.join(userInput[1:]))
            elif userCommand == commands[1]:
                sys.exit(0)
            elif userCommand == commands[2]:
                printDirectory(currDir)
            elif userCommand == commands[3]:
                pwd(currDir)
            elif userCommand == commands[4]:
                for command in commands:
                    print(command)
            elif userCommand == commands[5]:
                currDir = changeDir(currDir, userInput)
            elif userCommand == commands[6]:
               removeFileDir(currDir, userInput)
            elif userCommand == commands[7]:
                makeFile(userInput)
            else:
                print("Error: unkown command - type 'commands' for a list of "
                      "commands")
        except:
            print("Error: empty command")

def makeDir(input):
    os.mkdir(input)


def printDirectory(currDir):
    dir_entries = os.scandir(currDir)
    print('In Directory:')
    for entry in dir_entries:
        print(entry)


# pwd made a function to be used in multiple locations
def pwd(dir):
    print(dir)


def changeDir(currDir, userInput):
    if userInput[1] == 'prev':
        currDir = currDir.split('/')
        currDir = currDir[:len(currDir) - 1]
        currDir = '/'.join(currDir)
        os.chdir(currDir)
        pwd(currDir)

    else:
        temp = currDir
        for entry in os.listdir(currDir):
            if ' '.join(userInput[1:]) in entry and exists(
                    ' '.join(userInput[1:])):
                currDir += '/' + ' '.join(userInput[1:])
                os.chdir(currDir)
                pwd(currDir)
        if temp == currDir:
            print('no such directory exists')
    return currDir
def removeFileDir(currDir, userInput):
    found = False
    for entry in os.listdir(currDir):
        userIn = ' '.join(userInput[1:])
        if userIn in entry:
            found = True
            try:
                os.rmdir(userIn)
                print('Directory removed successfully')
            except:
                os.remove(userIn)
                print('File removed successfully')
    if not found:
        print("No such file or directory exists")
def makeFile(userInput):
    f = open(' '.join(userInput[1:]), 'w')
    f.close()
main()
