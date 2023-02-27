given_words = input().split(", ")
lst = input().split(", ")
substrings = []

for word in given_words:
    for current_word in lst:
        if word in current_word:
            substrings.append(word)
            break
print(substrings)