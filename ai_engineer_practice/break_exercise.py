numbers = [10, 20, 30, 40, 50, 60, 70]

target = []
for number in numbers:
    print(number)
    if number == 40:
        print("Target found")
        break

print("Search completed")