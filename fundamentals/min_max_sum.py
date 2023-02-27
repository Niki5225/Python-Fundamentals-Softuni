def min_num_finding(numbers):
    min_num = min(numbers)
    return min_num


def max_num_finding(numbers):
    max_num = max(numbers)
    return max_num


def sum_of_all_nums(numbers):
    sum_nums = 0
    for number in numbers:
        sum_nums += int(number)
    return sum_nums


int_nums = []
current_nums = input().split()
for num in current_nums:
    int_nums.append(int(num))
result_min = min_num_finding(int_nums)
result_max = max_num_finding(int_nums)
result_sum = sum_of_all_nums(int_nums)
print(f"The minimum number is {result_min}")
print(f"The maximum number is {result_max}")
print(f"The sum number is: {result_sum}")
