def move(current_message, num_letters):
    return current_message[num_letters:] + current_message[:num_letters]


def insert(current_message, current_index, current_value):
    return current_message[:current_index] + current_value + current_message[current_index:]


def change_all(current_message, current_substring, current_replacement):
    return current_message.replace(current_substring, current_replacement)


message = input()
command = input()
while True:
    if command == "Decode":
        break
    current_command = command.split("|")
    type_action = current_command[0]
    if type_action == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        message = change_all(message, substring, replacement)
    elif type_action == "Move":
        letters = int(current_command[1])
        message = move(message, letters)
    elif type_action == "Insert":
        index = int(current_command[1])
        value = current_command[2]
        message = insert(message, index, value)
    command = input()
print(f"The decrypted message is: {message}")