results = {}
command = input()
responses = {}
while True:
    if command == "exam finished":
        break
    current_command = command.split("-")
    username = current_command[0]
    if current_command[1] == "banned":
        needed_language = results[username][0]
        responses[needed_language] -= 1
        results[username].pop()
        continue
    else:
        language = current_command[1]
        points = int(current_command[2])
    if language not in responses.keys():
        responses[language] = 0
    responses[language] += 1
    if username not in results.keys():
        results[username] = [language, points]
    elif username in results.keys():
        if points > results[username][1]:
            results[username][1] = points
    command = input()
print("Results:")
for student, lst in results.items():
    result = lst[1]
    print(f"{student} | {result}")
print("Submissions:")
for current_language, response_num in responses.items():
    print(f"{current_language} - {response_num}")