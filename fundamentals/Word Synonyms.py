lines = int(input())
dictionary = {}
for current_line in range(lines):
    key = input()
    value = input()
    if key not in dictionary.keys():
        dictionary[key] = []
    dictionary[key].append(value)
for word,synonyms in dictionary.items():
    print(f"{word} - {', '.join(synonyms)}")