# Print even or odd numbers in a given range using recursion.

def even_odd(n, current = 1):
    if current > n:
        return
    if current % 2 == 0:
        print(f"Even : {current}")
    else:
        print(f"Odd : {current}")
    even_odd(n, current + 1)


num = int(input())
even_odd(num)