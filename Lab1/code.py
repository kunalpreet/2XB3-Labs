

def are_valid_groups(student_nos, groups):
    for student in student_nos:
        count = 0
        for group in groups:
            if student in group:
                count += 1
            
        if count != 1:
            return False

    return True

a = [1,2,3,4,5]
b = [[1,2], [3,4], [5]]
print(are_valid_groups(a,b))                
