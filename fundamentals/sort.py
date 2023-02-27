def sorting(numbers):
    numbers.sort()
    return list(numbers)


int_numbers = []
current_numbers = input().split()
for num in current_numbers:
    int_numbers.append(int(num))
print(sorting(int_numbers))



