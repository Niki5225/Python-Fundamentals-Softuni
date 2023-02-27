initial_energy = int(input())
command = input()
battles_counter = 0
while True:
    if command == "End of battle":
        won_game = True
        break
    distance = int(command)
    if initial_energy >= distance:
        initial_energy -= distance
        battles_counter += 1
    else:
        won_game = False
        break
    if battles_counter % 3 == 0:
        initial_energy += battles_counter
    command = input()
if won_game:
    print(f"Won battles: {battles_counter}. Energy left: {initial_energy}")
else:
    print(f"Not enough energy! Game ends with {battles_counter} won battles and {initial_energy} energy")