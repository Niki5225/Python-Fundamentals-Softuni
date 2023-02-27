strings = input().split(" ")
for word in strings:
    for current_word in range(len(word)):
        print(word, end="")