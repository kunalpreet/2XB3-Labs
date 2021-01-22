Answer = True

def are_valid_groups(student_nos, groups):
    for student in student_nos:
        for group in groups:
            if student in group:
                Answer = True
            else:
                Answer = False

                