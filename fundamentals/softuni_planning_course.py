def add_lesson(lesson_list, lesson):
    if lesson not in lesson_list:
        lesson_list.append(lesson)
    return lesson_list


def insert_lesson(lesson_list, lesson, index):
    if lesson not in lesson_list:
        lesson_list.insert(index, lesson)
    return lesson_list


def remove_lesson(lesson_list, lesson):
    if lesson in lesson_list:
        lesson_index = lesson_list.index(lesson)
        if lesson_index + 1 in range(len(lesson_list)):
            if "Exercise" in lesson_list[lesson_index + 1]:
                lesson_list.pop(lesson_index + 1)
        lesson_list.remove(lesson)
    return lesson_list


def swap_lessons(lesson_list, lesson1, lesson2):
    if lesson1 in lesson_list and lesson2 in lesson_list:
        first_position = lesson_list.index(lesson1)
        second_position = lesson_list.index(lesson2)
        first_has_exercise = False
        second_has_exercise = False
        if first_position + 1 in range(len(lesson_list)):
            first_has_exercise = "Exercise" in lesson_list[first_position + 1]
        if second_position + 1 in range(len(lesson_list)):
            second_has_exercise = "Exercise" in lesson_list[second_position + 1]
        lesson_list[first_position], lesson_list[second_position] = \
            lesson_list[second_position], lesson_list[first_position]
        if first_has_exercise and second_has_exercise:
            lesson_list[first_position + 1], lesson_list[second_position + 1] = \
                lesson_list[second_position + 1], lesson_list[first_position + 1]
        elif first_has_exercise and not second_has_exercise:
            lesson_list.insert(second_position + 1, lesson_list.pop(first_position + 1))
        elif not first_has_exercise and second_has_exercise:
            lesson_list.insert(first_position + 1, lesson_list.pop(second_position + 1))
    return lesson_list


def exercise(lesson_list, lesson):
    if lesson in lesson_list and f"{lesson}-Exercise" not in lesson_list:
        lesson_index = lesson_list.index(lesson)
        lesson_list.insert(lesson_index + 1, f"{lesson}-Exercise")
    elif lesson not in lesson_list:
        lesson_list.append(lesson)
        lesson_list.append(f"{lesson}-Exercise")
    return lesson_list


schedule = input().split(", ")
while True:
    command = input()
    if command == "course start":
        break
    current_command = command.split(":")
    action = current_command[0]
    if action == "Add":
        current_lesson = current_command[1]
        schedule = add_lesson(schedule, current_lesson)
    elif action == "Insert":
        current_lesson = current_command[1]
        current_index = int(current_command[2])
        schedule = insert_lesson(schedule, current_lesson, current_index)
    elif action == "Remove":
        current_lesson = current_command[1]
        schedule = remove_lesson(schedule, current_lesson)
    elif action == "Swap":
        first_lesson = current_command[1]
        second_lesson = current_command[2]
        schedule = swap_lessons(schedule, first_lesson, second_lesson)
    elif action == "Exercise":
        current_lesson = current_command[1]
        schedule = exercise(schedule, current_lesson)

for index, lesson in enumerate(schedule):
    print(f"{index + 1}.{lesson}")