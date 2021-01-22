

def are_valid_groups(student_nos, groups):
    for student in student_nos:
        Answer = 0
        for group in groups:
            if student in group:
                Answer += 1
            
        if Answer != 1:
            return False

    return True



a = [1, 2, 3, 4, 5]
b = [[1, 2], [3, 4], [5, 1]]
print(are_valid_groups(a, b))

