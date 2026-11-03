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

    
    
if choice == "3":
    print("Thanks for playing Mystery Island")





