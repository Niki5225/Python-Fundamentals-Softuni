
numbers = input().split()
int_numbers = []
for num in numbers:
    int_numbers.append(int(num))

result = filter(lambda x: x % 2 == 0, int_numbers)
print(list(result))