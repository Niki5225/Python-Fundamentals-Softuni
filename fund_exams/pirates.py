def plunder(the_dict, the_town, the_people, the_gold):
    the_dict[the_town][0] -= the_people
    the_dict[the_town][1] -= the_gold
    print(f"{the_town} plundered! {the_gold} gold stolen, {the_people} citizens killed.")
    if the_dict[the_town][0] <= 0 or the_dict[the_town][1] <= 0:
        print(f"{the_town} has been wiped off the map!")
        del the_dict[the_town]
    return the_dict


def prosper(the_dict, current_town, current_gold):
    if current_gold < 0:
        print(f"Gold added cannot be a negative number!")
    else:
        the_dict[current_town][1] += current_gold
        print(f"{current_gold} gold added to the city treasury."
              f" {current_town} now has {the_dict[current_town][1]} gold.")
    return the_dict


command = input()
pirates_treasury = {}
while True:
    if command == "Sail":
        break
    current_command = command.split("||")
    city = current_command[0]
    population = int(current_command[1])
    gold = int(current_command[2])
    if city not in pirates_treasury:
        pirates_treasury[city] = [population, gold]
    else:
        pirates_treasury[city][0] += population
        pirates_treasury[city][1] += gold
    command = input()
new_events = input()
while True:
    if new_events == "End":
        break
    current_new_events = new_events.split("=>")
    type_action = current_new_events[0]
    town = current_new_events[1]
    if type_action == "Plunder":
        new_people = int(current_new_events[2])
        new_gold = int(current_new_events[3])
        pirates_treasury = plunder(pirates_treasury, town, new_people, new_gold)
    elif type_action == "Prosper":
        new_gold = int(current_new_events[2])
        pirates_treasury = prosper(pirates_treasury, town, new_gold)

    new_events = input()
if len(pirates_treasury) > 0:
    print(f"Ahoy, Captain! There are {len(pirates_treasury)} wealthy settlements to go to:")
    for element in pirates_treasury:
        print(f"{element} -> Population: {pirates_treasury[element][0]} citizens, "
              f"Gold: {pirates_treasury[element][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
