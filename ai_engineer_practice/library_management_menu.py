choice = ""

while choice != "3":
    print("=============================================")
    print(     "WELCOME TO THE LIBRARY SYSTEM")
    print("=============================================")

    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. Exit")

    choice = input("Enter your choice")
    if choice == "1":
        print("You selected Borrow a Book")

    elif choice == "2":
        print("You selected Return a Book")

    elif choice == "3":
        print("Thank you for using our Library system")

    else:
        print("Invalid choice. Please try again.")


