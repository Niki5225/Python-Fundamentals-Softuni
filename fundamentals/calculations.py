def calculations(command, num1, num2):
    if command == 'multiply':
        return num1 * num2
    elif command == 'subtract':
        return num1 - num2
    elif command == 'add':
        return num1 + num2
    elif command == 'divide':
        return int(num1 / num2)


current_command = input()
number1 = int(input())
number2 = int(input())
print(calculations(current_command, number1, number2))