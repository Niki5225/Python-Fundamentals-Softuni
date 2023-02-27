import re

pattern = re.compile(r"([:]{2}|[*]{2})(?P<emoji>[A-Z][a-z]{2,})\1")
text = input()
total_coolness = 1
for element in text:
    if element.isdigit():
        total_coolness *= int(element)
result = list(pattern.finditer(text))
print(f"Cool threshold: {total_coolness}")
print(f"{len(result)} emojis found in the text. The cool ones are:")
for element in result:
    current_coolness = 0
    current_element = element["emoji"]
    for letter in current_element:
        current_coolness += ord(letter)
    if current_coolness >= total_coolness:
        print(element.group())
