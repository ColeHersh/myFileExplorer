import os
import sys

def main():
    print('Welcome to my file explorer terminal')
    commands = ['mkdir', 'exit', 'dir', 'pwd', 'commands', 'cd']
    currDir = 'C:/Users'
    userInput = ''
    while(True):
        userInput = input()
        userInput = userInput.split()
        userCommand = userInput[0]
        if userCommand == commands[0]:
           os.mkdir(userInput[1])
        elif userCommand == commands[1]:
            sys.exit(0)
        elif userCommand == commands[2]:
            dir_entries = os.scandir(currDir)
            print('In Directory:')
            for entry in dir_entries:
                print(entry)
        elif userCommand == commands[3]:
            print(currDir)
        elif userCommand == commands[4]:
            for command in commands:
                print(command)
        elif userCommand == commands[5]:
            temp = currDir
            for entry in os.listdir(currDir):
                if ' '.join(userInput[1:]) in entry:
                    currDir += '/' + ' '.join(userInput[1:])
            if temp == currDir:
                print('no such directory exists')
        else:
            print("Error: unkown command - type 'commands' for a list of "
                  "commands")
main()
