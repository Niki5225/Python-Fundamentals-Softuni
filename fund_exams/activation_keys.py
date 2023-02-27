def contains(current_activation_key, current_substring):
    if current_substring in current_activation_key:
        print(f"{current_activation_key} contains {substring}")
    else:
        print(f"Substring not found!")


def flip(current_activation_key, up_or_low, starting_index, ending_index):
    if up_or_low == "upper":
        current_activation_key = current_activation_key[:starting_index] + \
                                 current_activation_key[starting_index:ending_index].upper()\
                                 + current_activation_key[ending_index:]
        print(current_activation_key)
    elif up_or_low == "lower":
        current_activation_key = current_activation_key[:starting_index] + \
                                 current_activation_key[starting_index:ending_index].lower()\
                                 + current_activation_key[ending_index:]
        print(current_activation_key)
    return current_activation_key


def sliced(current_activation_key, start_index2, ending_index2):
    current_activation_key = current_activation_key[:start_index2] + current_activation_key[ending_index2:]
    print(current_activation_key)
    return current_activation_key


activation_key = input()
command = input()
while True:
    if command == "Generate":
        break
    current_command = command.split(">>>")
    type_action = current_command[0]
    if type_action == "Contains":
        substring = current_command[1]
        contains(activation_key, substring)
    elif type_action == "Flip":
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        upper_or_lower = ""
        if current_command[1] == "Lower":
            upper_or_lower = "lower"
            activation_key = flip(activation_key, upper_or_lower, start_index, end_index)
        else:
            upper_or_lower = "upper"
            activation_key = flip(activation_key, upper_or_lower, start_index, end_index)
    elif type_action == "Slice":
        starting_index1 = int(current_command[1])
        ending_index1 = int(current_command[2])
        activation_key = sliced(activation_key, starting_index1, ending_index1)
    command = input()
print(f"Your activation key is: {activation_key}")
