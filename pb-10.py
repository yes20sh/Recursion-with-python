# Reverse a string using recursion.
def reverse_str(text):
    if len(text) == 0:
        return ""
    return reverse_str(text[1:]) + text[0]

text = input()
print(reverse_str(text))