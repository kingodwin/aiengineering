student_age = 20
student_score = 65
application_submitted = True

admission_approved = (
    student_age >= 18
    and student_score >= 50
    and application_submitted
)

print(admission_approved)



has_exam_card = False
has_approved_id = True

print(has_exam_card or has_approved_id)


student_registered = False

print(not student_registered)
