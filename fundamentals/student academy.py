number_of_lines = int(input())
students = {}
for current_student in range(number_of_lines):
    name = input()
    grade = float(input())
    if name not in students.keys():
        students[name] = []
    students[name].append(grade)
for key, value in students.items():
    total_value = 0
    counter_notes = 0
    for element in value:
        total_value += float(element)
        counter_notes += 1
    final_note = total_value / counter_notes
    if final_note >= 4.50:
        print(f"{key} -> {final_note:.2f}")
