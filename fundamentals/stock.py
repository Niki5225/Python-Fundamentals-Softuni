items = input().split(" ")
searched_items = input().split(" ")
bakery = {}
for item in range(0, len(items), 2):
    key = items[item]
    value = int(items[item + 1])
    bakery[key] = value
for element in searched_items:
    all_keys = bakery.keys()
    if element in all_keys:
        value_of_element = bakery[element]
        print(f"We have {value_of_element} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")