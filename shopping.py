
'''Inventory Manager by Hamish Orr'''

open_file = open("items.csv", "r")
raw_text = open_file.read()
open_file.close()
raw_lines = raw_text.split('\n')
count = 0
items = []
while raw_lines[count] != '':
    item = raw_lines[count].split(',')
    items.append(item)
    count += 1

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
        print("Required Items:")
        print('')
        for i in range(len(items)):
            if items[i][3] == 'r':
                required_count += 1
                print("{:3} x {:20} at ${:6} each".format(items[i][2], items[i][0], items[i][1]))
                total_cost += float(items[i][2])*float(items[i][1])
        print('')
        print("Total Cost: ${}".format(total_cost))
        print('')
        if required_count == 0:
            print("All orders are complete! Choose another option.")
            print('')

    elif choice == 'C':
        complete_count = 0
        total_cost = 0
        print("Complete Orders:")
        print('')
        for i in range(len(items)):
            if items[i][3] == 'c':
                complete_count += 1
                print("{:3} x {:20}  at ${:6} each".format(items[i][2], items[i][0], items[i][1]))
                total_cost += float(items[i][2]) * float(items[i][1])
        print('')
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
            for i in range(len(items)):
                if name in items[i][0].upper():
                    match += 1
            if match == 0:
                print('Error! Item Not Found!')
                print('Name of complete item?')
                name = input(">>").upper()
        for i in range(len(items)):
            if items[i][0].upper() == name:
                items[i][3] = 'c'
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
            status = input('>>').upper()
        new_item = [name, price, quantity, status.lower()]
        print("New item saved!")
        items.append(new_item)

    else:
        print("Choice invalid!")

    save_file = open('items.csv', 'w')
    for i in range(len(items)):
        write_line = [items[i][0] + ',' + items[i][1] + ',' + items[i][2] + ',' + items[i][3] + '\n']
        save_file.writelines(write_line)
    save_file.close()

    print('MENU:')
    print("     R - Show list of required items")
    print("     C - Show list of completed items")
    print("     A - Add a new item")
    print("     M - Mark an item as complete")
    print("     Q - Quit")
    choice = input(">>").upper()
print("Thank-you for using Inventory control!")
  