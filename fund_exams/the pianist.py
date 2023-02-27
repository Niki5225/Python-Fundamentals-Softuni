def add(the_dict, curr_piece, curr_composer, curr_key):
    if curr_piece not in the_dict.keys():
        the_dict[curr_piece] = [curr_composer, curr_key]
        print(f"{curr_piece} by {curr_composer} in {curr_key} added to the collection!")
    else:
        print(f"{curr_piece} is already in the collection!")
    return the_dict


def remove(the_dict, curr_piece):
    if curr_piece in the_dict.keys():
        del the_dict[curr_piece]
        print(f"Successfully removed {curr_piece}!")
    else:
        print(f"Invalid operation! {curr_piece} does not exist in the collection.")
    return the_dict


def change_key(the_dict, curr_piece, curr_new_key):
    if curr_piece in the_dict:
        the_dict[curr_piece][1] = curr_new_key
        print(f"Changed the key of {curr_piece} to {curr_new_key}!")
    else:
        print(f"Invalid operation! {curr_piece} does not exist in the collection.")
    return the_dict


catalogue_with_pieces = {}
number = int(input())
for _ in range(number):
    inpt = input().split("|")
    the_piece = inpt[0]
    the_composer = inpt[1]
    the_key = inpt[2]
    if the_piece not in catalogue_with_pieces.keys():
        catalogue_with_pieces[the_piece] = [the_composer, the_key]
command = input()
while True:
    if command == "Stop":
        break
    current_command = command.split("|")
    type_action = current_command[0]
    piece = current_command[1]
    if type_action == "Add":
        composer = current_command[2]
        key = current_command[3]
        catalogue_with_pieces = add(catalogue_with_pieces, piece, composer, key)
    elif type_action == "Remove":
        catalogue_with_pieces = remove(catalogue_with_pieces, piece)
    elif type_action == "ChangeKey":
        new_key = current_command[2]
        catalogue_with_pieces = change_key(catalogue_with_pieces, piece, new_key)
    command = input()
for element in catalogue_with_pieces:
    print(f"{element} -> Composer: {catalogue_with_pieces[element][0]}, Key: {catalogue_with_pieces[element][1]}")
