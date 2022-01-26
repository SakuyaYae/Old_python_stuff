"""
the code Sakuyas inventory
"""
def invreadwhile(fd):
    """
    makes sure invread works
    """
    line = fd.read()
    print(line)
    return line

def invread():
    """
    open inventory to see whats inside
    """
    try:
        print("This is whats in my inventory")
        inventory = open("inv.data", "r")
        invreadwhile(inventory)
    except IOError:
        print("file not found")


def invadd(item):
    """
    Sakuya pick up a item an put it in the inventory
    """
    item = item + "\n"
    with open("inv.data", "a") as invadd1:
        invadd1.write(item)

def invdrop(item):
    """
    Sakuya drops items
    """

    inventory1 = open("inv.data", "r")
    inventory1 = invreadwhile(inventory1)
    if item in inventory1:
        with open("inv.data", "w") as invdrop1:
            inventory2 = inventory1.replace(item, "")
            invdrop1.write(inventory2)
    else:
        print("I dont have that item")


def invdropall():
    """
    Sakuya drops all items
    """
    line3 = input("Should I drop evrything? (yes/no) ")
    if line3 == "yes":
        with open("inv.data", "w") as invdrop2:
            invdrop2.write("")
