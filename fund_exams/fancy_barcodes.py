import re

pattern = re.compile(r"@([#]{1,})(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])@([#]{1,})")
number = int(input())
for _ in range(number):
    text = input()
    is_valid = False
    result = pattern.finditer(text)
    for data in result:
        group = "".join([num for num in data["barcode"] if num.isdigit()])
        is_valid = True
        if group:
            print(f"Product group: {group}")
        else:
            print("Product group: 00")
    if not is_valid:
        print("Invalid barcode")