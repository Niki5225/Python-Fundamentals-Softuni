items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split(" ")
obtained_legendary_material = False
while not obtained_legendary_material:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            items["shards"] -= 250
            obtained_legendary_material = True
            print("Shadowmourne obtained!")
        elif items["fragments"] >= 250:
            items["fragments"] -= 250
            obtained_legendary_material = True
            print("Valanyr obtained!")
        elif items["motes"] >= 250:
            items["motes"] -= 250
            obtained_legendary_material = True
            print("Dragonwrath obtained!")
        if obtained_legendary_material:
            break
    if obtained_legendary_material:
        break
    current_items = input().split(" ")
for material, quantity in items.items():
    print(f"{material}: {quantity}")
