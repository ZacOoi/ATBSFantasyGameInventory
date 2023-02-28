example_loot = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(myloot):
    total_items = 0
    for item in myloot.items():
        print(str(item[1]) + ' ' + str(item[0]))
        total_items += item[1]
    print('Total number of items: ' + str(total_items))


displayInventory(example_loot)