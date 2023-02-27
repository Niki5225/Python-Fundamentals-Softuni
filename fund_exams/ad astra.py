import re

text = input()
pattern = re.compile(r"([#|])(?P<item_name>[A-Za-z\s]+)"
                     r"\1(?P<expiration_date>[0-9]{2}/[0-9]{2}/[0-9]{2})"
                     r"\1(?P<calories>[0-9]{1,5})\1")

total_calories = 0
result = pattern.finditer(text)
final_result = []
for current_tuple in result:
    total_calories += int(current_tuple["calories"])
    final_result.append({"name": current_tuple["item_name"],
                         "date": current_tuple["expiration_date"],
                         "calories": current_tuple["calories"]})
print(f"You have food to last you for: {total_calories // 2000} days!")
for dictionary in final_result:
    print(f"Item: {dictionary['name']}, Best before: {dictionary['date']}, Nutrition: {dictionary['calories']}")
