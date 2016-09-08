
'''Inventory Manager by Hamish Orr'''

'''psudocode
open file
display list of options
while choice is not quit

    if choice is required items
    display the items containing 'r' in the status column
    display these items in an ordered list starting from priority 1 to 3 <<<still not ORDERED
    display number of items and total price

    if choice is complete items
    same as above but for complete

    if choice is mark as complete
    lookup item by number displayed <<< currently searches by name..

    if add item
    error check the user to enter numbers and letters where appropriate

    if quit
    quit and save the file'''

def main():

    items = open_file()
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
            required = 0
            total_cost = 0
            print("Required Items:")
            print('')
            for i in range(len(items)):
                if items[i][3] == 'r':
                    required += 1
                    print("{:3}.  {:18} $  {:6} ({:2})".format(required-1, items[i][0], format(float(items[i][1]), '.2f'), items[i][2]))
                    total_cost += float(float(items[i][1]))
            print('')
            print("Total expected price for {} items: ${}".format(required, total_cost))
            print('')
            if required == 0:
                print("All orders are complete! Choose another option.")
                print('')

        elif choice == 'C':
            complete = 0
            total_cost = 0
            print("Complete Orders:")
            print('')
            for i in range(len(items)):
                if items[i][3] == 'c':
                    complete += 1
                    print("{:3}.  {:18} $  {:6} ({:2})".format(complete-1, items[i][0], format(float(items[i][1]), '.2f'), items[i][2]))
                    total_cost += float(items[i][1])
            print('')
            print("Total expected price for {} items: ${}".format(complete, total_cost))
            print('')
            if complete == 0:
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

        elif choice.upper() == 'A':
            print("Item name?")
            name = input('>>')
            while name == '' or name.strip(' ') == '':
                print('Name input cannot be blank!')
                name = input('>>')

            form = False
            while not form:
                print("Item Price:")
                price = input('>>')
                check = price.replace('.', '0')
                if check != "".join(i for i in check if i in "0123456789"):
                    print('Please enter numbers! Letters are not accepted!')
                    form = False
                else:
                    form = True
            while float(price) < 0:
                print("Price cannot be negative!")
                price = input('>>')
            print("Priority(1-3) ?")
            priority = input('>>')
            while not priority.isdecimal():
                print("Please enter a positive integer from 1-3")
                priority = input('>>')
            while int(priority) < 1 or int(priority) > 3:
                print("Priority must 1, 2 or 3")
                priority = input('>>')
            status = 'R'
            new_item = [name, price, priority, status.lower()]
            print("New item saved!")
            items.append(new_item)
        else:
            print("Choice invalid!")

        print('MENU:')
        print("     R - Show list of required items")
        print("     C - Show list of completed items")
        print("     A - Add a new item")
        print("     M - Mark an item as complete")
        print("     Q - Quit")
        choice = input(">>").upper()
    save_file(items)
    print("Thank-you for using Inventory control!")


def open_file():
    file = open('items.csv', "r")
    items = []
    line = file.readline().strip('\n')
    while line != '':
        items.append(line.split(','))
        line = file.readline().strip('\n')
    file.close()
    return items


def save_file(lines):
    file = open('items.csv', 'w')
    for i in range(len(lines)):
        line = ','.join(lines[i]) + '\n'
        file.writelines(line)
    file.close()
    return 'Any changes have been saved!'


main()

