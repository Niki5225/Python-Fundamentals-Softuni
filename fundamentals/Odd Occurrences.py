elements = input().split(" ")
dict = {}
for word in elements:
    current_word = word.lower()
    if current_word not in dict:
        dict[current_word] = 0
    dict[current_word] += 1
for key, value in dict.items():
    if value % 2 != 0:
        print(key, end=" ")