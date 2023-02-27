entry = input()
phonebook = {}
while True:
    if "-" not in entry:
        break
    username, phone_number = entry.split("-")
    phonebook[username] = phone_number
    entry = input()
for name in range(int(entry)):
    current_name = input()
    if current_name in phonebook.keys():
        print(f"{current_name} -> {phonebook[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")
