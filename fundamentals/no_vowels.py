word = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [letter for letter in word if letter.lower() not in vowels]
print("".join(result))