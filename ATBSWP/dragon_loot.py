# updates inventory from dragon's loot

def add_to_inventory(inventory, loot):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

def display_inventory(inventory):
    for k, v in inventory.items():
        print(f"{v} {k}")
        
inv = {'gold coin' : 42, 'rope' : 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)