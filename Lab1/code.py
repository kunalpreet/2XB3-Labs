

<<<<<<< HEAD
def are_valid_groups(studentNums, groups):
    a = len(studentNums)
    for i in studentNums:
        count = 0
        for j in groups:
            if i in j:
                count = count + 1
=======
def are_valid_groups(student_nos, groups):
    for student in student_nos:
        count = 0
        for group in groups:
            if student in group:
                count += 1
            
        if count != 1:
            return False

    return True

>>>>>>> 72838f943382ec070fbdf6885aced17a52f41354

    if count == a:
        return True
    return False

a = [1, 2, 3, 4, 5]
<<<<<<< HEAD
b = [[1, 2], [3, 4], [1]]
=======
b = [[1, 2], [3, 4], [5]]
>>>>>>> 72838f943382ec070fbdf6885aced17a52f41354
print(are_valid_groups(a, b))
                