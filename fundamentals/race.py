import re

participants = input().split(", ")
command = input()
while True:
    if command == "end of race":
        break
    current_command = command

    command = input()