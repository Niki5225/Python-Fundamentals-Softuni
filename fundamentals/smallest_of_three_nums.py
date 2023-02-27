def smallest_of_three_nums(num1, num2, num3):
    smallest_num = num1
    if smallest_num > num2:
        smallest_num = num2
    if smallest_num > num3:
        smallest_num = num3
    return smallest_num


number1 = int(input())
number2 = int(input())
number3 = int(input())
print(smallest_of_three_nums(number1, number2, number3))
