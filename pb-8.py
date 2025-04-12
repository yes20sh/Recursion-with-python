# Find the GCD of two numbers using recursion.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input("Enter two number: ").split())
print(gcd(a, b))