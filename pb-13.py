# Convert a decimal number to binary using recursion.

def convert_binary(n):
    if n == 0:
        return ""
    return convert_binary(n // 2) + str(n % 2)

n = int(input("Enter the number : "))
print(f"Binary number of {n} is {convert_binary(n)}")        