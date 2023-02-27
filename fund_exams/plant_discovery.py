def rate(the_dict, current_plant, current_rating):
    if current_plant not in the_dict.keys():
        print("error")
        return the_dict
    the_dict[current_plant][1].append(current_rating)
    return the_dict


def update(the_dict, current_plant, current_rarity):
    if current_plant not in the_dict.keys():
        print("error")
        return the_dict
    the_dict[current_plant][0] = current_rarity
    return the_dict


def reset(the_dict, current_plant):
    if current_plant not in the_dict.keys():
        print("error")
        return the_dict
    the_dict[current_plant][1] = []
    return the_dict


number = int(input())
plants = {}
for num in range(number):
    inp = input().split("<->")
    given_plant = inp[0]
    rarity = inp[1]
    plants[given_plant] = [rarity, []]

command = input()
while True:
    if command == "Exhibition":
        break
    current_command = command.split(": ")
    type_action = current_command[0]
    if type_action == "Rate":
        data = current_command[1].split(" - ")
        plant = data[0]
        rating = int(data[1])
        plants = rate(plants, plant, rating)
    elif type_action == "Update":
        data = current_command[1].split(" - ")
        plant = data[0]
        new_rarity = int(data[1])
        plants = update(plants, plant, new_rarity)
    elif type_action == "Reset":
        plant = current_command[1]
        plants = reset(plants, plant)
    command = input()
print(f"Plants for the exhibition:")
for key in plants:
    average_rating = 0
    if sum(plants[key][1]) != 0:
        average_rating = sum(plants[key][1]) / len(plants[key][1])
    print(f"- {key}; Rarity: {plants[key][0]}; Rating: {average_rating:.2f}")
