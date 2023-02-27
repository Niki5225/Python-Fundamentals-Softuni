number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

his_attendance = 0
max_bonus = 0

for current_student in range(1, number_of_students + 1):
    attendance = int(input())

    total_bonus = (attendance / number_of_lectures) * (5 + additional_bonus)
    if max_bonus <= total_bonus:
        max_bonus = total_bonus
        if attendance >= number_of_lectures:
            his_attendance = number_of_lectures
        else:
            his_attendance = attendance

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {round(his_attendance)} lectures.")
