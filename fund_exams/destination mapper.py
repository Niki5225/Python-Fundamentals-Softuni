import re

text = input()
pattern = re.compile(r"([/=])(?P<destination>[A-Z][A-Za-z]{2,})\1")
result = pattern.finditer(text)
destinations = 0
lst = []

for current_destination in result:
    lst.append(current_destination["destination"])

for element in lst:
    destinations += len(element)

print(f"Destinations: {', '.join(lst)}")
print(f"Travel Points: {destinations}")
