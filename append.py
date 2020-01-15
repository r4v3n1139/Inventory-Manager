def addItem():
    response = input('Would you like to add an item? [y/n] ')
    if response == 'N':
        response = 'n'
    while response != 'n':
        getInput()
        response = input('Would you like to add another item? [y/n] ')
        if response == 'N':
            response = 'n'

def getInput():
    name = input('Please enter item Name: ')
    desc = input('Please enter item Description: ')
    qty = input('Please enter the quantity: ')
    print('------------------------')
    print('Name:', name)
    print('Description:', desc)
    print('Quantity:', qty)
    print('------------------------')
    writeToFile(name, desc, qty)

def writeToFile(name, desc, qty):
    file_output = open('Data List.txt', 'a')
    file_output.write(name + '\n')
    file_output.write(desc + '\n')
    file_output.write(qty + '\n')
    file_output.close()