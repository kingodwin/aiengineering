student_name = ""
student_score = 0

while student_score != -1 :
    print("===============================================")
    print(           "STUDENT SCORE SYSTEM")
    print("===============================================")


    student_name = input("Enter student name:")
    student_score = int(input("Enter score (-1 to stop):"))

    if student_score == -1:
        break

    elif student_score < 0 or student_score > 100:
        print("Invalid score")
        continue

    elif student_score >= 70:
        print(f"{student_name} received Grade A")


    elif student_score >= 60:
        print(f"{student_name} received Grade B")

    elif student_score >= 50:
        print(f"{student_name} received Grade C")

    elif student_score >= 45:
        print(f"{student_name} received Grade D")

    elif student_score >= 0:
        print(f"{student_name} received Grade F")

    else:
        print("Invalid score")
        print("Score processing stopped.")
        