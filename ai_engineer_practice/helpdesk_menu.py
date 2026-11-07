choice = ""

while choice != "3":
    print("=======================================")
    print(    "WELCOME TO CAMPUS HELPDESK")
    print("=======================================")

    print("1. Create a Ticket")
    print("2. View Ticket")
    print("3. Quit")

    choice = input("Enter your choice:")
    if choice == "1":
        print("You selected Create Ticket")

    elif choice == "2":
        print("You selected View Ticket")

    elif choice == "3":
        print("Thank you for using Campus Helpdesk!")

    else:
        print("Invalid choice.  Please try again.")