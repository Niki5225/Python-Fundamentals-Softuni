bdef take_odd(current_password):
    current_password = current_password[1::2]
    print(current_password)
    return current_password


def cut(current_password, current_index, current_length):
    current_password = current_password[:index] + current_password[index + length:]
    print(current_password)
    return current_password


def substitute(current_password, current_substring, current_substitution):
    if current_substring in current_password:
        current_password = current_password.replace(current_substring, current_substitution)
        print(current_password)
    else:
        print(f"Nothing to replace!")
    return current_password


password = input()
command = input()
while True:
    if command == "Done":
        break
    current_command = command.split(" ")
    type_action = current_command[0]
    if type_action == "TakeOdd":
        password = take_odd(password)
    elif type_action == "Cut":
        index = int(current_command[1])
        length = int(current_command[2])
        password = cut(password, index, length)
    elif type_action == "Substitute":
        substring = current_command[1]
        substitution = current_command[2]
        password = substitute(password, substring, substitution)
    command = input()
print(f"Your password is: {password}")
