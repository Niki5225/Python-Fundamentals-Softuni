def even_odd_sum(number):
    sum_of_odd_nums = 0
    sum_of_even_nums = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_nums += int(digit)
        else:
            sum_of_odd_nums += int(digit)
    return sum_of_even_nums, sum_of_odd_nums


number_as_a_string = input()
sum_even, sum_odd = even_odd_sum(number_as_a_string)
print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")