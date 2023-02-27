def cast_spell(the_dict, current_hero, mana, spell):
    if the_dict[current_hero][1] >= mana:
        the_dict[current_hero][1] -= mana
        print(f"{current_hero} has successfully cast {spell} and now has {the_dict[current_hero][1]} MP!")
    else:
        print(f"{current_hero} does not have enough MP to cast {spell}!")
    return the_dict


def take_damage(the_dict, current_hero, done_damage, current_attacker):
    the_dict[current_hero][0] -= done_damage
    if the_dict[current_hero][0] > 0:
        print(f"{current_hero} was hit for {done_damage} HP by {current_attacker} and now has "
              f"{the_dict[current_hero][0]} HP left!")
    else:
        print(f"{current_hero} has been killed by {current_attacker}!")
        del the_dict[current_hero]
    return the_dict


def recharge(the_dict, current_hero, current_amount):
    starting_mana = the_dict[current_hero][1]
    if starting_mana + current_amount > 200:
        the_dict[current_hero][1] = 200
        print(f"{current_hero} recharged for {200 - starting_mana} MP!")
    else:
        the_dict[current_hero][1] += current_amount
        print(f"{current_hero} recharged for {current_amount} MP!")
    return the_dict


def heal(the_dict, current_hero, current_hp):
    starting_hp = the_dict[current_hero][0]
    if starting_hp + current_hp > 100:
        the_dict[current_hero][0] = 100
        print(f"{current_hero} healed for {100 - starting_hp} HP!")
    else:
        the_dict[current_hero][0] += amount_hp
        print(f"{current_hero} healed for {amount_hp} HP!")
    return the_dict


num_heroes = int(input())
heroes = {}
for _ in range(num_heroes):
    hero, hp, mp = input().split(" ")
    heroes[hero] = [int(hp), int(mp)]
command = input()
while True:
    if command == "End":
        break
    current_command = command.split(" - ")
    type_action = current_command[0]
    hero_name = current_command[1]
    if type_action == "CastSpell":
        mp_needed = int(current_command[2])
        spell_name = current_command[3]
        heroes = cast_spell(heroes, hero_name, mp_needed, spell_name)
    elif type_action == "TakeDamage":
        damage = int(current_command[2])
        attacker = current_command[3]
        heroes = take_damage(heroes, hero_name, damage, attacker)
    elif type_action == "Recharge":
        amount_mana = int(current_command[2])
        heroes = recharge(heroes, hero_name, amount_mana)
    elif type_action == "Heal":
        amount_hp = int(current_command[2])
        heroes = heal(heroes, hero_name, amount_hp)
    command = input()
for key in heroes:
    print(f"{key}")
    print(f"  HP: {heroes[key][0]}")
    print(f"  MP: {heroes[key][1]}")
