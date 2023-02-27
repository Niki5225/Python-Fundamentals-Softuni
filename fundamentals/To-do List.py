notes = []
while True:
    command = input()
    if command == "End":
        break
    current_command = command.split("-")
    priority = int(current_command[0])
    task = current_command[1]
    notes.append((priority, task))
sorted_notes = [sorted_data[1] for sorted_data in sorted(notes)]
print(sorted_notes)