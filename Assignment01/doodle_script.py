'''def choose_complete(items)
    required = 0
    required_list = []
    total_cost = 0
    print("Required Items:")
    print('')
    for i in range(len(items)):
        if items[i][3] == 'r':
            required += 1
            required_list.append(required - 1, items[i][0], items[i][1],items[i][2])
            print("{:3}.  {:18} $  {:6} ({:})".format(required - 1, items[i][0], format(float(items[i][1]), '.2f'),
                                                      items[i][2]))
            total_cost += float(float(items[i][1]))
    Print('')
    Print('Which item is complete?')
    item_number = input('>>')
    while item_number'''

