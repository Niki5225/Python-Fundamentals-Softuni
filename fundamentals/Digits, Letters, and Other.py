string = input()
text = ''
digits = ''
other = ''
for element in string:
    if element.isalpha():
        text += element
    elif element.isdigit():
        digits += element
    else:
        other += element
print(digits)
print(text)
print(other)