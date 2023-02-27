import re

search_pattern = r"\b(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"

dates = input()

result = re.findall(search_pattern, dates)

x = [print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}") for match in result]