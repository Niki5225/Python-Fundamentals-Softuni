def insert_space(current_message, current_index):
    current_message = current_message[:current_index] + " " + current_message[current_index:]
    print(current_message)
    return current_message


def reverse(current_message, current_substring):
    if current_substring in current_message:
        current_message = current_message.replace(current_substring, "", 1)
        current_substring = current_substring[::-1]
        current_message = current_message + current_substring
        print(current_message)
    else:
        print("error")
    return current_message


def change_all(current_message, current_substring, current_replacement):
    current_message = current_message.replace(current_substring, current_replacement)
    print(current_message)
    return current_message


message = input()
command = input()
while True:
    if command == "Reveal":
        break
    current_command = command.split(":|:")
    type_action = current_command[0]
    if type_action == "InsertSpace":
        index = int(current_command[1])
        message = insert_space(message, index)
    elif type_action == "Reverse":
        substring = current_command[1]
        message = reverse(message, substring)
    elif type_action == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        message = change_all(message, substring, replacement)
    command = input()
print(f"You have a new text message: {message}")
