# Print 1 to N without loops

def print_num(n):   
    if not n:
        return 
    print_num(n - 1)
    print(n)

n = int(input())
print_num(n)