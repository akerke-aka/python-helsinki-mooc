""" Course grading, part 1
--------------------------
Reads student information data and exercise completion data from two CSV files.
Returns the total number of exercises completed by each student.

Steps:
- reads student names and IDs from file
- reads exercise completion data from file
- aggregates and prints results
"""

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

# dictionary for student IDs -> name
names = {}
with open(student_info) as new_file:    
    for line in new_file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        else:
            names[parts[0]] = parts[1] + " " + parts[2]
# dictionary for student IDs -> total exercises
exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        else:
            grades_sum = sum(int(value) for value in parts[1:])
            exercises[parts[0]]=grades_sum
# print summary
for id, name in names.items():
    if id in exercises:
        grades_sum = exercises[id]
        print(f"{name} {grades_sum}")
