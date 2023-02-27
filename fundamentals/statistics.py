bakery = {}
total_quantity = 0
while True:
    command = input()
    if command == "statistics":
        break
    product = command.split(": ")
    current_product = product[0]
    value = int(product[1])
    total_quantity += value
    if current_product in bakery:
        bakery[current_product] += value
    else:
        bakery[current_product] = value
print(f"Products in stock:")
for key, current_value in bakery.items():
    print(f"- {key}: {current_value}")
print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {total_quantity}")
