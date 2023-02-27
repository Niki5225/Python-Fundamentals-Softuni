def rounding_numbers(numbers):
    for num in numbers:
        current_num = float(num)
        rounded_nums_lst.append(round(current_num))


given_numbers = input().split(" ")
rounded_nums_lst = []
rounding_numbers(given_numbers)
print(rounded_nums_lst)
