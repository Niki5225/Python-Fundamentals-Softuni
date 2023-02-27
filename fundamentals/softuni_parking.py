number_of_commands = int(input())
parking = {}
for command in range(number_of_commands):
    current_command = input().split(" ")
    if current_command[0] == "register":
        username = current_command[1]
        license_plate_number = current_command[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif current_command[0] == "unregister":
        username = current_command[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")
