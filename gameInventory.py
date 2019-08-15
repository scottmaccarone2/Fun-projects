# Suppose you are creating a fantasy game. The data structure to model the
# player's inventory will be a dictionary where the keys are string values
# describing the item in the inventory and the value is an integer value
# detailing how many of that item the player has. For example:
# inventory = {'gold coin': 13, 'dagger': 2, 'sword': 3}
# Write a function that would take any possible "inventory" and display it
# nicely.

if __name__ == "__main__":

    def displayInventory(inventory):
        print("Inventory:")
        item_total = 0
        for k, v in inventory.items():
            item_total = item_total + v
            print(v, k)
        print("Total number of items: " + str(item_total))

# Suppose, in addition, that upon "slaying the dragon", you obtain additional
# loot, maybe something like this:
# dragonLoot = ['rope', 'torch', 'gold coin', 'gold coin', 'rope', 'ruby']
# Write a function accepting two parameters: an inventory dictionary, and a
# list-like argument containing additional items to update or include into
# the inventory. The function should return a dictionary representing the
# updated inventory.

    def addToInventory(inventory, addedItems):
        print("Updated Inventory: ")
        for item in addedItems:
            inventory.setdefault(item, 0)
            inventory[item] = inventory[item] + 1
        displayInventory(inventory)
