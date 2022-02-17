#Begin! Menu page
print('Welcome to battle game! \n(1)new game\n(2)save game\n(3)quit')

def main():
    selection = input('Choose your option')
    if selection.upper() == '1':
        new_game()              
    elif selection.upper() == '2':
        print('Loading save game...')
        pass
    elif selection.upper() == '3':
        print('Exit game...')
        pass
    else:
        print("You entered the wrong option")
        return main()
