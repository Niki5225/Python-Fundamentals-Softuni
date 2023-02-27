list_of_chars = input().split(", ")
values_dict = {key: ord(key) for key in list_of_chars}
print(values_dict)