def add(current_wagons, current_people):
    current_wagons[-1] += current_people
    return current_wagons


def leave(current_wagons, current_index, current_people):
    current_wagons[current_index] -= current_people
    return current_wagons


def insert(current_wagons, current_index, current_people):
    current_wagons[current_index] += current_people
    return current_wagons


wagons = int(input())
wagons_list = [int(0) for _ in range(wagons)]
new_command = input()
while True:
    if new_command == "End":
        break
    command = new_command.split(" ")
    type_of_command = command[0]
    if type_of_command == "add":
        people = int(command[1])
        wagons_list = add(wagons_list, people)
    elif type_of_command == "leave":
        index = int(command[1])
        people = int(command[2])
        wagons_list = leave(wagons_list, index, people)
    elif type_of_command == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons_list = insert(wagons_list, index, people)
    new_command = input()
print(wagons_list)
