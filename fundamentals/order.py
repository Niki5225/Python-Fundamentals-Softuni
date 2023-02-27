command = input()
products = {}
while True:
    if command == "buy":
        break
    orders = command.split(" ")
    name = orders[0]
    price = float(orders[1])
    quantity = int(orders[2])
    if name not in products.keys():
        products[name] = [price, quantity]
    if name in products.keys():
        for current_name in products.keys():
            if current_name == name:
                products[current_name][0] = price
                products[current_name][1] += quantity
    command = input()
for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
