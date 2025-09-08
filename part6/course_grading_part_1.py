
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

names = {}
with open(student_info) as new_file:    
    for line in new_file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        else:
            names[parts[0]] = parts[1] + " " + parts[2]

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        else:
            grades_sum = sum(int(value) for value in parts[1:])
            exercises[parts[0]]=grades_sum
for id, name in names.items():
    if id in exercises:
        grades_sum = exercises[id]
        print(f"{name} {grades_sum}")