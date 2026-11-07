student_age = 21
student_score = 75
application_submitted = True
student_suspended = False


student_eligible = (
    student_age >= 18
    and student_score >= 50
    and application_submitted
    and not student_suspended
)
print(student_eligible)