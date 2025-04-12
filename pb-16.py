# Check if a given string is a palindrome using recursion.

def is_palindrome(text, current = 0):
    if current >= len(text) // 2:
        return True
    if text[current] != text[-(current + 1)]:
        return False
    return is_palindrome(text, current + 1)

text = input()
if is_palindrome(text):
    print("Yes, It is palindrome")
else:
    print("No, It is not palindrome")

