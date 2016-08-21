print('')
print("Welcome to Inventory Manager by Hamish Orr")
print('')
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

''' to index the 'ith' column in the 'jth' row >>>  items[j][i]'''

print('MENU:')
print("     R - Show list of required items")
print("     C - Show list of completed items")
print("     A - Add a new item")
print("     M - Mark an item as complete")
print("     Q - Quit")
choice = input(">>").upper()

while choice != 'Q':

    if choice == 'R':
        required_count = 0
        total_cost = 0
        for i in range(0, rows):
            if 'r' in items[i][3]:
                required_count += 1
                print("Required: {:1} x {:15} at ${:6} each".format(items[i][2], items[i][0], items[i][1]))
                total_cost += float(items[i][2])*float(items[i][1])
        print("Total Cost: ${}".format(total_cost))
        print('')
        if required_count == 0:
            print("All orders are complete! Choose another option.")
            print('')

    elif choice == 'C':
        complete_count = 0
        total_cost = 0
        for i in range(0,rows):
            if 'c' in items[i][3]:
                complete_count += 1
                print("Order complete: {:1} x {:15}  at ${:6} each".format(items[i][2], items[i][0], items[i][1]))
                total_cost += float(items[i][2]) * float(items[i][1])
        print("Total Charges: ${}".format(total_cost))
        print('')
        if complete_count == 0:
            print("No complete orders! Choose another option.")
            print('')

    elif choice == 'M':
        print('Name of complete item?')
        match = 0
        name = input(">>").upper()
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

    elif choice == 'A':
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
        rows += 1

    else:
        print("Choice invalid!")
    save_file = open('items.csv', 'w')

    for i in range(0, len(items)):
        line = [items[i][0] + ',' + items[i][1] + ',' + items[i][2] + ',' + items[i][3]]
        save_file.writelines(line)
    save_file.close()

    print('MENU:')
    print("     R - Show list of required items")
    print("     C - Show list of completed items")
    print("     A - Add a new item")
    print("     M - Mark an item as complete")
    print("     Q - Quit")
    choice = input(">>").upper()
print("Thank-you for using Inventory control!")
