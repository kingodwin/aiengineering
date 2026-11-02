player_name = input("What is your name")

energy = 5

location = "Beach"

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
        print("You begin exploring the Beach.")
        print("You discover something interesting")

    elif choice == "2":
        print("Your inventory is currently empty.")


if choice == "3":
    print("Thanks for playing Mystery Island")





