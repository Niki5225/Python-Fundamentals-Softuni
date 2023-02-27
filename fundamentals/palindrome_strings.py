words = input().split(" ")
palindrome_words = [element for element in words if ''.join(reversed(element)) == element]
searched_palindrome = input()
print(palindrome_words)
print(f"Found palindrome {palindrome_words.count(searched_palindrome)} times")