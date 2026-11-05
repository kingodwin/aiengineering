name = input("Enter your name:")
price_per_note = int(input("Enter notebook price:"))
note_books = int(input("Enter quantity:"))


total = price_per_note * note_books
print(f"Customer: {name}")
print(f"Total payment: #{total:,}")
