def positive(nums):
    positives = [num for num in nums if int(num) >= 0]
    return positives


def negative(nums):
    negatives = [num for num in nums if int(num) < 0]
    return negatives


def odd(nums):
    odds = [num for num in nums if int(num) % 2 != 0]
    return odds


def even(nums):
    evens = [num for num in nums if int(num) % 2 == 0]
    return evens


numbers = input().split(", ")
print(f"Positive: {', '.join(positive(numbers))}")
print(f"Negative: {', '.join(negative(numbers))}")
print(f"Even: {', '.join(even(numbers))}")
print(f"Odd: {', '.join(odd(numbers))}")
