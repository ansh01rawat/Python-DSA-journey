inventory = {}
def add_item():
    item = input("name of item = ")
    quantity = int(input("no. of pieces = "))
    if item not in inventory:
        inventory[item] = quantity
        print("item added successfully")
def search_item():
    item = input("name of item = ")
    if item in inventory:
        print(f"{item}:{inventory[item]} units")
    else:
        print("item not available")
def delete_item():
    item = input("name of item = ")
    if item in inventory:
        del inventory[item]
        print("item deleted successfully")
    else:
        print("item not found")
def display_inventory():
    if not inventory:
        print("inventory not found")
        return
    print("\ninventory")
    for item,quantity in inventory.items():
        print(f"{item}:{quantity}")

def menu():
    while True:

        print("\n=======inventory management=======")
        print("1.Add item")
        print("2.Search item")
        print("3.Delete item")
        print("4.Display inventory")
        print("5.Close program")

        choice = int(input("enter your choice = "))

        if choice == 1:
            add_item()
        elif choice == 2:
            search_item()
        elif choice == 3:
            delete_item()
        elif choice == 4:
            display_inventory()
        elif choice == 5:
            print("exiting program...")
        else:
            print("invalid choice.Try again")

menu()


