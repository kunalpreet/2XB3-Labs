

def are_valid_groups(student_nos, groups):
    for student in student_nos:
        count = 0
        
        for group in groups:
            count2 = 0
            for x in group:
                count2 += 1
            if count2 > 3 or count2 < 2:
                return False
            if student in group:
                count += 1
            
        if count != 1:
            return False

    return True

a = ["1", "2", "3", "4", "5", "6"]
b = [["1", "2"], ["4", "3"], ["5", "6"]]
print(are_valid_groups(a, b))
                
