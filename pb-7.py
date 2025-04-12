# Find the sum of digits of a number using recursion.

def sum_digit(num):
    if num < 10:
        return num
    return num % 10 + sum_digit(num // 10)
num = int(input())
print(sum_digit(num))