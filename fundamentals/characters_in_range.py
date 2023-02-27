def characters_returning(first_char, second_char):
    char_sequence_list = []
    for current_char in range(ord(first_char) + 1, ord(second_char)):
        char_sequence_list.append(chr(current_char))
    return char_sequence_list


char1 = input()
char2 = input()
result = characters_returning(char1, char2)
print(" ".join(result))