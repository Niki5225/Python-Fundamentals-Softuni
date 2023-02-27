def cheat(command):
    for _ in range(2):
        sequence_of_elements.insert(len(sequence_of_elements) // 2, f'-{number_of_moves}a')
    return "Invalid input! Adding additional elements to the board"


def right_choice(index1, index2):
    number = sequence_of_elements[int(first_index)]
    sequence_of_elements.remove(number)
    sequence_of_elements.remove(number)
    return f"Congrats! You have found matching elements - {number}!"


def wrong_choice():
    print("Try again!")


sequence_of_elements = input().split()
command = input()
middle = len(sequence_of_elements) // 2
number_of_moves = 0
while command != "end":
    choice = command.split()
    number_of_moves += 1
    first_index = choice[0]
    second_index = choice[1]
    if first_index == second_index or int(first_index) > len(sequence_of_elements) - 1 \
            or int(second_index) > len(sequence_of_elements) - 1 or int(first_index) < 0 or int(second_index) < 0:
        print(cheat(choice))
    elif sequence_of_elements[int(first_index)] == sequence_of_elements[int(second_index)]:
        print(right_choice(first_index, second_index))
    elif sequence_of_elements[int(first_index)] != sequence_of_elements[int(second_index)]:
        wrong_choice()
    if len(sequence_of_elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break
    command = input()
if len(sequence_of_elements) != 0:
    print(f"Sorry you lose :(")
    sequence_of_elements = " ".join(sequence_of_elements)
    print(f"{sequence_of_elements}")