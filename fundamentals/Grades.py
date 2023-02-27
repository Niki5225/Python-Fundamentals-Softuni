def grade(number):
    if 2 <= number <= 2.99:
        return 'Fail'
    elif 3 <= number <= 3.49:
        return 'Poor'
    elif 3.50 <= number <= 4.49:
        return 'Good'
    elif 4.50 <= number <= 5.49:
        return 'Very Good'
    else:
        return 'Excellent'


current_number = float(input())
print(grade(current_number))
