# =====================================
# MYSTERY ISLAND: THE LOST LIGHTHOUSE
# =====================================

from game_logic import get_next_location, can_enter_location

play_again = "1"

while play_again == "1":

    # RESET GAME VARIABLES
    player_name = input("What is your name? ")

    energy = 5
    location = "Beach"
    inventory = []
    game_over = False
    choice = ""

    # GAME INTRODUCTION
    print("==============================")
    print("     MYSTERY ISLAND")
    print("    THE LOST LIGHTHOUSE")
    print("==============================")

    print("\nGAME INSTRUCTIONS")
    print("1. Explore the island to collect useful items.")
    print("2. Collect a Rope to cross the Old Bridge.")
    print("3. Collect a Lantern to enter the Lighthouse.")
    print("4. Each successful movement costs 1 energy.")
    print("5. Your decisions can increase or reduce your energy.")
    print("6. Reach the Lighthouse before your energy runs out.")

    print(f"\nWelcome, {player_name}!")
    print(f"Current Location: {location}")
    print(f"Energy: {energy}")

    # MAIN GAME LOOP
    while choice != "3" and not game_over:

        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Check inventory")
        print("3. Quit")
        print("4. Travel to another location")

        choice = input("Choose an option: ")

        # EXPLORE
        if choice == "1":

            if "Rope" not in inventory:
                inventory.append("Rope")
                print("You found a Rope!")

            elif "Lantern" not in inventory:
                inventory.append("Lantern")
                print("You found a Lantern!")

            else:
                print("You have collected all available items!")

        # CHECK INVENTORY
        elif choice == "2":

            print("Your inventory:", inventory)

        # QUIT
        elif choice == "3":

            print("You have decided to quit the adventure.")

        # TRAVEL
        elif choice == "4":

            if location == "Lighthouse":

                print("You have already reached the final destination!")

            else:

                destination = input("Where would you like to go? ")

                next_location = get_next_location(location)

                # CHECK CORRECT ROUTE
                if destination != next_location:

                    print(
                        f"Wrong route! From {location}, "
                        f"you must travel to {next_location}."
                    )

                # CHECK ROPE REQUIREMENT
                elif not can_enter_location(destination, inventory):

                    if destination == "Old Bridge":
                        print("You need a Rope to cross the bridge!")

                    elif destination == "Lighthouse":
                        print("You need a Lantern to enter the Lighthouse!") 

                # SUCCESSFUL TRAVEL
                else:

                    location = destination

                    print(f"\nYou have travelled to the {location}!")
                    print(f"Current Location: {location}")

                    # REDUCE ENERGY FOR TRAVELLING
                    energy -= 1

                    # JUNGLE DECISION
                    if location == "Jungle":

                        print("\nYou have reached the Jungle!")
                        print("1. Take the safe path")
                        print("2. Take the dangerous shortcut")

                        jungle_choice = input("Choose your path: ")

                        if jungle_choice == "1":

                            print("You took the safe path. No extra energy lost.")

                        elif jungle_choice == "2":

                            energy -= 2
                            print("You took the dangerous shortcut and lost 2 energy!")

                        else:

                            print("Invalid choice. You lost 1 extra energy.")
                            energy -= 1

                    # CAVE DECISION
                    elif location == "Cave":

                        print("\nYou have reached the Cave!")
                        print("1. Search for an energy supply")
                        print("2. Ignore the supply and continue")

                        cave_choice = input("Choose an option: ")

                        if cave_choice == "1":

                            energy += 2
                            print("You found an energy supply! You gained 2 energy.")

                        elif cave_choice == "2":

                            print("You ignored the energy supply.")

                        else:

                            print("Invalid choice. You lost 1 extra energy.")
                            energy -= 1

                    # OLD BRIDGE DECISION
                    elif location == "Old Bridge":

                        print("\nYou have reached the Old Bridge!")
                        print("1. Cross the bridge carefully")
                        print("2. Return to the Cave and prepare")

                        bridge_choice = input("Choose an option: ")

                        if bridge_choice == "1":

                            energy -= 1
                            print("You crossed the bridge carefully.")
                            print("You lost 1 extra energy.")

                        elif bridge_choice == "2":

                            location = "Cave"
                            energy += 1

                            print("You decided to return to the Cave.")
                            print("Your energy has been restored for this journey.")

                        else:

                            print("Invalid choice. You lost 1 extra energy.")
                            energy -= 1

                    # DISPLAY ENERGY
                    print(f"\nEnergy: {energy}")

                    # CHECK GAME OVER
                    if energy <= 0:

                        print("\nGAME OVER!")
                        print("You have run out of energy.")
                        game_over = True

                    # CHECK WINNING CONDITION
                    elif location == "Lighthouse" and "Lantern" in inventory:

                        print("\n==============================")
                        print("     CONGRATULATIONS!")
                        print("YOU HAVE FOUND THE LOST LIGHTHOUSE!")
                        print("           YOU WIN!")
                        print("==============================")

                        game_over = True

        # INVALID MENU CHOICE
        else:

            print("Invalid choice! Please select 1, 2, 3, or 4.")

    # END OF GAME
    print("\nThanks for playing Mystery Island!")

    # REPLAY SYSTEM
    play_again = input(
        "Would you like to play again? (1 = Yes, 2 = No): "
    )

    while play_again not in ["1", "2"]:

        print("Invalid choice. Please enter 1 or 2.")

        play_again = input(
            "Would you like to play again? (1 = Yes, 2 = No): "
        )

    if play_again == "1":

        print("\nStarting a new adventure!")

    else:

        print("Thanks for your adventure. Goodbye!")