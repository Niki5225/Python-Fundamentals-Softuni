def drive(the_dict, current_car, the_distance, the_fuel):
    if the_dict[current_car][1] < the_fuel:
        print("Not enough fuel to make that ride")
    else:
        the_dict[current_car][0] += the_distance
        the_dict[current_car][1] -= the_fuel
        print(f"{current_car} driven for {the_distance} kilometers. {the_fuel} liters of fuel consumed.")
    if the_dict[current_car][0] >= 100000:
        print(f"Time to sell the {current_car}!")
        the_dict.pop(current_car)
    return the_dict


def refuel(the_dict, current_car, the_fuel):
    starting_fuel = the_dict[current_car][1]
    if starting_fuel + the_fuel > 75:
        the_dict[current_car][1] = 75
        print(f"{current_car} refueled with {75 - starting_fuel} liters")
    else:
        print(f"{current_car} refueled with {the_fuel} liters")
        the_dict[current_car][1] = starting_fuel + the_fuel
    return the_dict


def revert(the_dict, current_car, given_kilometers):
    starting_kilometers = the_dict[current_car][0]
    if starting_kilometers - given_kilometers < 10000:
        the_dict[current_car][0] = 10000
    else:
        print(f"{current_car} mileage decreased by {given_kilometers} kilometers")
        the_dict[current_car][0] = starting_kilometers - given_kilometers
    return the_dict


number_of_cars = int(input())
cars = {}
for _ in range(number_of_cars):
    command = input().split("|")
    new_car = command[0]
    new_mileage = int(command[1])
    new_fuel = int(command[2])
    cars[new_car] = [new_mileage, new_fuel]
command = input()
while True:
    if command == "Stop":
        break
    current_command = command.split(" : ")
    type_action = current_command[0]
    car = current_command[1]
    if type_action == "Drive":
        distance = int(current_command[2])
        fuel = int(current_command[3])
        cars = drive(cars, car, distance, fuel)
    elif type_action == "Refuel":
        fuel = int(current_command[2])
        cars = refuel(cars, car, fuel)
    elif type_action == "Revert":
        kilometers = int(current_command[2])
        cars = revert(cars, car, kilometers)
    command = input()
for element in cars:
    print(f"{element} -> Mileage: {cars[element][0]} kms, Fuel in the tank: {cars[element][1]} lt.")
