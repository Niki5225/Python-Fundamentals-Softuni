import re

sentence = input()
word = input()

pattern = fr"\b{word}\b"

res = re.findall(pattern, sentence, flags=re.IGNORECASE)
print(len(res))
