

def are_valid_groups(studentNums, groups):
    a = len(studentNums)
    for i in studentNums:
        count = 0
        for j in groups:
            if i in j:
                count = count + 1

    if count == a:
        return True
    return False

a = [1, 2, 3, 4, 5]
b = [[1, 2], [3, 4], [1]]
print(are_valid_groups(a, b))
                