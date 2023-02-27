def replace(text, char, n_char):
    text = text.replace(char, n_char)
    print(text)
    return text


def cut(text, index1, index2):
    if 0 <= index1 <= len(text) - 1 and 0 <= index2 <= len(text) - 1:
        text = text[:index1] + text[index2 + 1::]
        print(text)
    else:
        print("Invalid indices!")
    return text


def make(text, upper_lower):
    if upper_lower == "upper":
        text = text.upper()
    else:
        text = text.lower()
    print(text)
    return text


def check(text, subtext):
    if subtext in text:
        print(f"Message contains {subtext}")
    else:
        print(f"Message doesn't contain {subtext}")


def summ(text, s_index, e_index):
    if 0 <= s_index < len(text) - 1 and 0 <= e_index < len(text) - 1:
        current_subtext = text[s_index:e_index + 1]
        total_value = 0
        for element in current_subtext:
            total_value += ord(element)
        print(total_value)
    else:
        print("Invalid indices!")


string = input()
while True:
    line = input()
    if line == "Finish":
        break
    command = line.split()
    type_action = command[0]
    if type_action == "Replace":
        current_char = command[1]
        new_char = command[2]
        string = replace(string, current_char, new_char)
    elif type_action == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        string = cut(string, start_index, end_index)
    elif type_action == "Make":
        upper_lower = command[1].lower()
        string = make(string, upper_lower)
    elif type_action == "Check":
        substring = command[1]
        check(string, substring)
    elif type_action == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        summ(string, start_index, end_index)
