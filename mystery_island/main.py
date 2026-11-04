player_name = input("What is your name")

energy = 5

location = "Beach"

inventory = []

game_over = False

allowed_routes = {
    "Beach": "Jungle",
    "Jungle": "Cave",
    "Cave": "Old Bridge",
    "Old Bridge": "Lighthouse"
}


print("==============================")
print("     MYSTERY ISLAND     ")
print("    THE LOST LIGHTHOUSE")
print("==============================")


print(f"Welcome, {player_name}!")
print(f"Current Location: {location}")
print(f"Energy: {energy}")

choice = ""

while choice != "3" and not game_over:
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

        next_location = allowed_routes.get(location)

        if destination == "Lighthouse":
            print("You have reached the final destination!")
            

        if destination != next_location:
            print(f"Wrong route! From {location}, you must travel to {next_location}.")

        elif destination == "Old Bridge" and "Rope" not in inventory:
            print("You need a Rope to cross the bridge!")

        elif destination == "Lighthouse" and "Lantern" not in inventory:
            print("You need a Lantern to enter the Lighthouse!")

        else:
            location = destination
            print(f"You have travelled to the {location}!")
            print(f"Current Location: {location}")

            energy -= 1
            print(f"Energy: {energy}")


            if energy <= 0:
                print("GAME OVER! You run out of energy.")
                game_over = True  

            elif location == "Lighthouse" and "Lantern" in inventory:
                print("CONGRATULATIONS! YOU HAVE FOUND THE LIGHTHOUSE!")
                print("YOU WIN!")
                game_over =  True 
    else:
        if choice != "3":
            print("Invalid choice! Please select 1, 2, 3, 4.")



    
if choice == "3":
    print("Thanks for playing Mystery Island")

