def sum_numbers(num1, num2):
    return num1 + num2


def add_and_subtract(num1, num2, num3):
    return sum_numbers(first_num, second_num) - num3


first_num = int(input())
second_num = int(input())
third_num = int(input())
result = add_and_subtract(first_num, second_num, third_num)
print(result)
