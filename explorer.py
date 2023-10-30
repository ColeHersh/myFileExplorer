import os


def main():
    currDir = 'C:/Users'
    userInput = ''
    while(userInput != 'exit'):
        userInput = input()
main()
print(os.listdir('C:/Users'))