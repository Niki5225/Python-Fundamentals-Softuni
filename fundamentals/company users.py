company = {}
command = input()
while True:
    if command == "End":
        break
    current_command = command.split(" -> ")
    current_company = current_command[0]
    id = current_command[1]
    if current_company not in company.keys():
        company[current_company] = []
    if id not in company[current_company]:
        company[current_company].append(id)
    command = input()
for key, value in company.items():
    print(key)
    for element in value:
        print(f"-- {element}")
