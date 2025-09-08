""" 
Course grading, part 2
----------------------
Reads three SCV files: students, exercises, exam points.
- student_info: student IDs and name
- exercise_data: total exercises completed by each student
- exam_points: exam points for each student

Steps:
- read all three SCV files and matches student by their ID
- calculate total exercise points
- add exercise points to exam points
- converts total points into a grade
- print the student name and their final grade
"""

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")

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
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        else:
            grades_sum = sum(int(value) for value in parts[1:])
            exercises[parts[0]]=grades_sum

# dictionary for student IDs -> exam points
exam_p = {}
with open(exam_points) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        else:
            points_sum = sum(int(value) for value in parts[1:])
            exam_p[parts[0]] = points_sum
            
#convert number of exercises to exercise points
def exe_points(total_exe):
    return ((total_exe*10) // 40)

#convert total points to grade
def grade_from_total(total):
    if total <= 14: return 0
    if total <= 17: return 1
    if total <= 20: return 2
    if total <= 23: return 3
    if total <= 27: return 4
    return 5
    
#print results  
for id, name in names.items():                 
    if id not in exercises or id not in exam_p:
        continue                               

    exercise_pts = exe_points(exercises[id]) # exercises points
    exam_pts = exam_p[id]                    # exam points  
    total_points = exercise_pts + exam_pts   # total points
    grade = grade_from_total(total_points)   # final grade     

    print(f"{name} {grade}")
