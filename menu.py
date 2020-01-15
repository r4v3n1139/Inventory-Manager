import append
import search

def main():
    response = 0
    while response != 3:
        print('Data List Manager')
        print('------MENU------')
        print('[1] Add Item')
        print('[2] Search for an item')
        print('[3] Exit')
        response = int(input('>> '))
        if response == 1:
            append.addItem()
        elif response == 2:
            search.inquiry()
        elif response == 3:
            print('Goodbye :)')
        else:
            print('Please enter a valid selection.')

main()
