''' By Hamish Orr,  URL: https://github.com/hamishorr/Assignments

    pseudocode

    open file
    display list of options
        while choice is not quit
            if choice is required items
                if all items are complete print "no required items"
                display the items containing 'r' in the status column
                display these items in an ordered list starting from priority 1 to 3
                display number of items and total price

            if choice is complete items
                same as above but for complete

            if choice is mark as complete
                if all items are already complete print "no required items"
                lookup item by number displayed (ascending order)
                save the item as complete and display a notification

            if add item
                error check the user to enter numbers and letters where appropriate
                add the new item to the main items list
        when choice is to quit
                save the file, displaying the number of items saved
                display closing message

'''


def main():
    items = open_file()
    display_menu()
    choice = input(">>").upper()

    while choice != 'Q':
        if choice == 'R':
            required_list = status_list(items, 'r')
            if not required_list:
                print("No required items!")
            else:
                display(required_list)

        elif choice == 'C':
            complete_list = status_list(items, 'c')
            if not complete_list:
                print("No complete items!")
            else:
                display(complete_list)

        elif choice == 'M':
            required_list = status_list(items, 'r')
            if not required_list:
                print("No required items!")
            else:
                display(required_list)
                print('Enter the number of an item to mark as complete')
                priority_correct = False
                while not priority_correct:
                    item_number = input('>>')
                    if is_empty(item_number):
                        print('Invalid input; enter a number')
                    elif not item_number.isdecimal() or not is_numbers(item_number):
                        print('Invalid input; enter a number')
                    elif int(item_number) < 0:
                        print('Invalid item number')
                    elif not int(item_number) <= len(required_list) - 1:
                        print('Invalid item number')
                    else:
                        priority_correct = True
                        required_list[int(item_number)][3] = 'c'
                        print('{} marked as complete'.format(required_list[int(item_number)][0]))

        elif choice == 'A':
            new_item = create_lists(4)
            print("Item name?")
            name = input('>>')
            while is_empty(name):
                print('Invalid input; enter a name')
                name = input('Input name:')
            new_item[0] = name
            price_correct = False
            while not price_correct:
                price = input('Price:$')
                if is_empty(price):
                    print('Invalid input; enter a valid number')
                elif not is_numbers(price):
                    print('Invalid input; enter a valid number')
                elif float(price) < 0:
                    print('Invalid input; enter a valid number')
                else:
                    price_correct = True
                    new_item[1] = price
            print("Priority:")
            priority_correct = False
            while not priority_correct:
                priority = input('>>')
                if is_empty(priority):
                    print("Priority must 1, 2 or 3")
                elif not priority.isdecimal() or not is_numbers(priority):
                    print("Priority must 1, 2 or 3")
                elif int(priority) < 1 or int(priority) > 3:
                    print("Priority must 1, 2 or 3")
                else:
                    priority_correct = True
                    new_item[2] = priority
            new_item[3] = 'r'
            print("{}, ${} (priority {}) added to shopping list".format(new_item[0], format(float(new_item[1])
                                                                                            , '.2f'), new_item[2]))
            items.append(new_item)

        else:
            print("Invalid menu choice")

        display_menu()
        choice = input(">>").upper()

    save_file(items)
    print("{} items saved to items.csv".format(len(items)))
    print("Have a nice day :)")


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


def is_numbers(string):
    check = string.replace('.', '0')
    if check != "".join(i for i in check if i in "0123456789"):
        return False
    else:
        return True


def status_list(main_list, status):
    read_list = []
    for i in range(len(main_list)):
        if main_list[i][3] == status:
            read_list.append(main_list[i])
    if not read_list:
        ordered_list = []
    else:
        from operator import itemgetter
        ordered_list = sorted(read_list, key=itemgetter(2))
    return ordered_list


def display_menu():
    print('MENU:')
    print("R - Show list of required items")
    print("C - Show list of completed items")
    print("A - Add a new item")
    print("M - Mark an item as complete")
    print("Q - Quit")


def display(lines):
    total_cost = 0
    for i in range(len(lines)):
        print("{}.  {:18} $  {:5} ({})".format(i, lines[i][0], format(float(lines[i][1]), '.2f'), lines[i][2]))
        total_cost += float(lines[i][1])
    print("Total expected price for {} items: ${}".format(len(lines), total_cost))


def create_lists(number):
    new_list = []
    for i in range(number):
        new_list.append([])
    return new_list


def is_empty(string):
    while string == '' or string.strip(' ') == '':
        return True
    else:
        return False


main()
