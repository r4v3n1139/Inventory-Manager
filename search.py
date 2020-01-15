def inquiry():
    response = input('Would you like to search for an item? [y/n] ')
    if response == 'N':
        response = 'n'
    while response != 'n':
        search = input('Please enter item name: ')
        lookUp(search)
        response = input('Would you like to search for another item? [y/n] ')
        if response == 'N':
            response = 'n'

def lookUp(search):
    found = False
    file = open('Data List.txt', 'r')
    name = (file.readline()).rstrip('\n')
    while name != '':
        desc = (file.readline()).rstrip('\n')
        qty = int((file.readline()).rstrip('\n'))
        if search == name:
            found = True
            print('------------------------')
            print('Name:', name)
            print('Description:', desc)
            print('Quantity:', qty)
            print('------------------------')
        name = (file.readline()).rstrip('\n')
    file.close()
    if not found:
        print('That item was not found.')

