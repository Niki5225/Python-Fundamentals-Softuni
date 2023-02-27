def prefect_number_check(num):
    sum_divisors = 0
    if num > 0:
        for divisor in range(1, num + 1):
            if num % divisor == 0:
                sum_divisors += divisor
    if sum_divisors // 2 == int(num):
        return True
    else:
        return False


number = int(input())
result = prefect_number_check(number)
if result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
