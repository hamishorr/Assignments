
'''Scan file for number of rows to create list'''
items_file = open("items.csv", "r")
rows = 0
while items_file.readline() != '':
    rows += 1
items = list(range(0, rows))
items_file.close()

'''Save list of items to memory'''
items_file = open("items.csv", "r")
for i in range(0, rows):
    items[i] = items_file.readline().split(',')
items_file.close()

print(items)

''' this indexes the 'nth' column in the 'ith' row >>>(items[i][n])'''

''' this divides the 'ith' row up by it's commas >>> items[i].split(',')'''

print("Welcome to the Inventory")
print('MENU:')
print("     R - Show list of required items")
print("     C - Show list of completed items")
print("     A - Add a new item")
print("     M - Mark an item as complete")
print("     Q - Quit")
choice = input(">>").upper()

while choice != 'Q':

    if choice == 'M':
        print('Name of complete item?')
        name = input(">>").upper()

        match = 0
        while match == 0:
            for i in range(0, rows):
                if name in items[i][0].upper():
                    match += 1
            if match == 0:
                print('Error! Item Not Found!')
                print('Name of complete item?')
                name = input(">>").upper()

        for i in range(0, rows):
            if items[i][0].upper() == name:
                items[i][3] = 'c\n'

        print('Item marked as complete!')

    if choice == 'A':
        print("Item name?")
        name = input('>>')

        print("Item price?")
        price = (input('>>'))
        while str(price).isdecimal():
            print("Please enter price in $$.cc format.")
            price = input('>>')

        print("Quantity?")
        quantity = input('>>')
        while not str(quantity).isdecimal():
            print("Please enter the exact quantity: (eg. 1,2,3,4...)")
            quantity = input('>>')

        print("Required or Complete? enter 'R' or 'C'")
        status = input('>>').upper()

        if status == 'R' or 'C':
            pass
        else:
            print("Error! Required or Complete? enter 'R' or 'C'")
            status = input('>>')

        new_item = [name, price, quantity, status.lower() + '\n']
        print("New item saved!")

        items += [new_item]

    save_file = open('items_new.csv', 'w')

    for i in range(0, len(items)):
        line = [items[i][0] + ',' + items[i][1] + ',' + items[i][2] + ',' + items[i][3]]
        save_file.writelines(line)
    save_file.close()

    '''print(items)'''
    print('MENU:')
    print("     R - Show list of required items")
    print("     C - Show list of completed items")
    print("     A - Add a new item")
    print("     M - Mark an item as complete")
    print("     Q - Quit")
    choice = input(">>")
print("Thank-you for using Inventory control!")






items_file.close()

'''print("Welcome to the Inventory")

items_file = open("items.csv", "r")

items = items_file.readline()
while items_file.readline() != '':
    items += items_file.readline()
items_file.close()

items




print(items)

items_file.close()'''