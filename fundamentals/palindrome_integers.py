def checking_for_palindrome_nums(numbers):
    for current_number in numbers:
        reversed_number = str(current_number[::-1])
        if reversed_number == current_number:
            print(True)
        else:
            print(False)


current_numbers = input().split(", ")
checking_for_palindrome_nums(current_numbers)
