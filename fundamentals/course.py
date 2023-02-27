students = {}
command = input()
while True:
    if command == "end":
        break
    current_command = command.split(" : ")
    course_name = current_command[0]
    student = current_command[1]
    if course_name not in students.keys():
        students[course_name] = []
    students[course_name].append(student)
    command = input()
for key, value in students.items():
    print(f"{key}: {len(students[key])}")
    for item in value:
        print(f"-- {item}")
