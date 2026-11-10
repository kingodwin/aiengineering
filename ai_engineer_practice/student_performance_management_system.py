student_name = ""
student_score = 0
students = []

while student_name != "done":
    print("=======================================================")
    print("STUDENT PERFORMANCE MANAGEMENT SYSTEM")
    print("=======================================================")

    student_name = input("Enter student name: ")

    if student_name.lower() == "done":
        break

    student_score = -1

    # SCORE VALIDATION
    while student_score < 0 or student_score > 100:
        student_score = int(input("Enter a valid score: "))

        if student_score < 0 or student_score > 100:
            print("Invalid score. Please try again.")

    # GRADE ASSIGNMENT
    if student_score >= 70:
        grade = "A"

    elif student_score >= 60:
        grade = "B"

    elif student_score >= 50:
        grade = "C"

    elif student_score >= 45:
        grade = "D"

    else:
        grade = "F"

    print(f"{student_name} scored {student_score}")
    print(f"{student_name} received Grade {grade}")

    # CREATE STUDENT RECORD
    student = {
        "name": student_name,
        "score": student_score,
        "grade": grade
    }

    # STORE STUDENT RECORD
    students.append(student)

print("\nStudent registration stopped.")

print("\nALL STUDENT RECORDS:")
print(students)