
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")

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
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        else:
            exe_nmb = sum(int(value) for value in parts[1:])
            exercises[parts[0]]=exe_nmb

exam_p = {}

with open(exam_points) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        else:
            points_sum = sum(int(value) for value in parts[1:])
            exam_p[parts[0]] = points_sum

def exe_points(total_exe):
    return ((total_exe*10) // 40)

def grade_from_total(total):
    if total <= 14: return 0
    if total <= 17: return 1
    if total <= 20: return 2
    if total <= 23: return 3
    if total <= 27: return 4
    return 5

print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
    
for id, name in names.items():                 
    if id not in exercises or id not in exam_p:
        continue                               
    exe_nmb = exercises[id]
    exercise_pts = exe_points(exercises[id])   
    exam_pts = exam_p[id]                      
    total_points = exercise_pts + exam_pts
    grade = grade_from_total(total_points)        
    
    print(f"{name:30}{exe_nmb:<10}{exercise_pts:<10}{exam_pts:<10}{total_points:<10}{grade:<10}")
