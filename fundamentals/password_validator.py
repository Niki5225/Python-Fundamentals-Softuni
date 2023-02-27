def length_pass_checker(password):
    if 6 > len(password) or len(password) > 10:
        messages.append("Password must be between 6 and 10 characters")


def symbols_in_pass(password):
    if not password.isalnum():
        messages.append("Password must consist only of letters and digits")


def minimum_digits(password):
    counter = 0
    for symbol in password:
        if symbol.isdigit():
            counter += 1
    if counter < 2:
        messages.append("Password must have at least 2 digits")


messages = []
current_password = input()
length_pass_checker(current_password)
symbols_in_pass(current_password)
minimum_digits(current_password)
if len(messages) == 0:
    print("Password is valid")
else:
    for message in messages:
        print(message)
