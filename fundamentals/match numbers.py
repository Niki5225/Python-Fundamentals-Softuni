import re
search_pattern = r"(^|(?<=\s))-?(\d+)(\.\d+)?($|(?=\s))"

text = input()

result = re.finditer(search_pattern, text)
for match in result:
    print(match.group(), end=" ")