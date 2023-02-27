initial_list = input().split("!")
command = input()
while True:
    if command == "Go Shopping!":
        break
    else:
        command = command.split()
    type_command = command[0]
    if type_command == "Urgent":
        item = command[1]
        if item not in initial_list:
            initial_list.insert(0, item)
    elif type_command == "Unnecessary":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)
    elif type_command == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in initial_list:
            for index in range(len(initial_list)):
                if initial_list[index] == old_item:
                    initial_list[index] = new_item
                    break
    elif type_command == "Rearrange":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
    command = input()
print(", ".join(initial_list))