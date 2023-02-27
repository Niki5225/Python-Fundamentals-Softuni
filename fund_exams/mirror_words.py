import re

pattern = re.compile(r"([@|#])(?P<word>[A-Za-z]{3,})\1\1(?P<mirror_word>[A-Za-z]{3,})\1")
text = input()

result = pattern.finditer(text)

mirror_words_dict = {}

for element in result:
    mirror_words_dict[element["word"]] = element["mirror_word"]

if len(mirror_words_dict) == 0:
    print("No word pairs found!")
else:
    print(f"{len(mirror_words_dict)} word pairs found!")
valid_pairs = []
for key, value in mirror_words_dict.items():
    if key == value[::-1]:
        valid_pairs.append(f"{key} <=> {value}")
if not valid_pairs:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(valid_pairs))
