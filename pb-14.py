# Check if a number is a prime number using recursion.

def is_prime(n, i =2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if i % n == 0:
        return False
    return is_prime(n, i + 1)

num = int(input())
if is_prime(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")
