words = "".join(input().split(" "))
dictionary = {}
for element in words:
    if element not in dictionary.keys():
        dictionary[element] = 0
    dictionary[element] += 1
for key, value in dictionary.items():
    print(f"{key} -> {value}")