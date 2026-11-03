player_name = input("What is your name")

energy = 5

location = "Beach"

inventory = []


print("==============================")
print("     MYSTERY ISLAND     ")
print("    THE LOST LIGHTHOUSE")
print("==============================")


print(f"Welcome, {player_name}!")
print(f"Current Location: {location}")
print(f"Energy: {energy}")

choice = ""

while choice != "3":
    print("\nWhat would you like to do?")
    print("1. Explore")
    print("2. Check inventory")
    print("3. Quit")
    print("4. Travel to another location")

    choice = input("Choose an option:")

    if choice == "1":
        if "Rope" not in inventory:
            inventory.append("Rope")
            print("You found a Rope!")

        elif "Lantern" not in inventory:
            inventory.append("Lantern")
            print("You found a Lantern!")

    elif choice == "2":
        print("Your inventory:", inventory)

    elif choice == "4":
        destination = input("Where would you like to go? ")

        if destination == "Jungle":
            location = "Jungle"
            print("You have travelled to the Jungle!")
            print(f"Current Location: {location}")

        elif destination == "Cave":
            location = "Cave"
            print("You have travelled to the Cave")
            print(f"Current Location: {location}")

        elif destination == "Old Bridge":
            location = "Old Bridge"
            print("You have travelled to the Old Bridge")
            print(f"Current Location: {location}")

        elif destination == "Lighthouse":
            if "Lanter" in inventory:
                location = "Lighthouse"
                print("You have travelled to the Lighthouse")
                print(f"Current Location: {location}")
            else:
                print("You need a Lanter to enter the Lighouse")
                


        else:
            print("That location is not available.")


    
if choice == "3":
    print("Thanks for playing Mystery Island")

