"""Fantasy Game Inventory"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)


print()


"""List To Dictionary Function For Fantasy Game Inventory"""

def addtoInventory(inventory, addedItems):
    for loot in addedItems:
        inventory.setDefault(loot, 0)
        inventory[loot] += 1
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)                
