def comma_code(list):
    if list == []:
        print("List is empty.\n")
    
    elif len(list) >= 2:
        print("'", end='')
        for item in list[0:-1]:
            print(f"{item}, ", end='')
        print(f"and {list[-1]}'")

    else:
        print(f"'{list[0]}'")

kaufen_list = []
while True:
    print('Inform an item to put on the list (hit enter to quit): ')
    new_list_item = input('> ')
    
    new_list_item.strip()

    if new_list_item == '':
        print('Oh, to be a weenie...\n')
        break
    elif new_list_item:
        kaufen_list.append(new_list_item)
        print('Done, next!\n')
        continue
    else:
        print('Please, type something.\n')
        continue

comma_code(kaufen_list)
