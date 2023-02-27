import re
searched_pattern = r"\d+"
while True:
    sentences = input()
    if sentences:
        result = re.findall(searched_pattern, sentences)
        if result:
            print(" ".join(result), end=" ")
    else:
        break
