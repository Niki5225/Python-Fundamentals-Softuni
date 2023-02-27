happiness = list(map(int, input().split(" ")))
factor = int(input())
multiplied = []
for num in happiness:
    element = factor * num
    multiplied.append(element)
total = 0
for element in multiplied:
    total += element
average = total // len(multiplied)
counter_more_average = 0
for particle in multiplied:
    if particle > average:
        counter_more_average += 1
if counter_more_average >= len(multiplied) // 2:
    print(f"Score: {counter_more_average}/{len(multiplied)}. Employees are happy!")
else:
    print(f"Score: {counter_more_average}/{len(multiplied)}. Employees are not happy!")