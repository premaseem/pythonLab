
for i in range(3):
    password = input('Enter password: ')
    if password == 'secret':
        print('You guessed the password!')
        break
else:
    print('3 incorrect password attempts')