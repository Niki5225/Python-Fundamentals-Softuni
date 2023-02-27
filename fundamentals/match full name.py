import re

search_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

names = input()

result = re.findall(search_pattern, names)

print(" ".join(result))
