import re

search_pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\b\d{3}-\d{4}\b"

phones = input()

result = re.findall(search_pattern, phones)
print(", ".join(result))