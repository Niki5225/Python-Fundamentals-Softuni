import re

number = int(input())
pattern = re.compile(r"([\w|\W]+)>(?P<one>[0-9]{3})\|(?P<two>[a-z]{3})\|"
                     r"(?P<three>[A-Z]{3})\|(?P<four>[^<>]{3})<\1")
for _ in range(number):
    password = input()
    result = pattern.finditer(password)
    is_valid = False
    for data in result:
        encrypted_password = data["one"] + data["two"] + data["three"] + data["four"]
        is_valid = True
        print(f"Password: {encrypted_password}")
    if not is_valid:
        print("Try another password!")