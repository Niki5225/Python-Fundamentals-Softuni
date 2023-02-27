def add_stop(current_stops, current_index, current_string):
    if 0 <= current_index < len(current_stops):
        current_stops = current_stops[:current_index] + current_string + current_stops[current_index:]
    print(current_stops)
    return current_stops


def remove_stop(current_stops, current_start, current_end):
    if 0 <= current_start < len(current_stops) and 0 <= current_end < len(current_stops):
        current_stops = current_stops[:current_start] + current_stops[current_end + 1:]
    print(current_stops)
    return current_stops


def switch(current_stops, old_string, new_string):
    if old_string in current_stops:
        current_stops = current_stops.replace(old_string, new_string)
    print(current_stops)
    return current_stops


stops = input()
command = input()
while True:
    if command == "Travel":
        break
    current_command = command.split(":")
    type_action = current_command[0]
    if type_action == "Add Stop":
        index = int(current_command[1])
        string = current_command[2]
        stops = add_stop(stops, index, string)
    elif type_action == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        stops = remove_stop(stops, start_index, end_index)
    elif type_action == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        stops = switch(stops, old_string, new_string)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")
