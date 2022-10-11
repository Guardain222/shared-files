invetory  = ["book", "map", "grande", "pistol", "Fees of Tutiton"]
i = invetory
# ask player would u like to add the sword in the inventory 
quesiton = str(input("Would u like to add the sword of Azeroth to your inventory?: "))
if quesiton == "yes" or quesiton == "y":
    invetory.append("Sword of Azeroth")
    print ("The sword has been added to your inventory")
    print ("This is your new inventory", invetory)
    print ("You are carrying", len(invetory), "ammounts of item")
else:
    print ("The sword was not added to your inventory")
# ask player if they would like to remove fees of tutition
remove_question = str(input("Would you like to remove the Fees of Tutition"))
if remove_question == "Yes" or remove_question == "y":
    invetory.remove(4)
    print ("The item has been removed")
    print ("This is your new inventory", invetory)
else:
    print ("The item has not been removed")

