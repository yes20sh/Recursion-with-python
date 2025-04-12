# Factorial

def factorial(n):
    if not n:
        return 1
    return factorial(n-1) * n

n = int(input())
print(factorial(n))