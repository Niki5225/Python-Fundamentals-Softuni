import re

pattern = r"\b_([A-Za-z0-9]+)\b"

sentence = input()

res = re.findall(pattern, sentence)
print(",".join(res))