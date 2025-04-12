# Check if an array is sorted using recursion.

def arr_sort(arr, current = 0):
    if current == len(arr) - 1:
        return True
    if arr[current] > arr[current + 1]:
        return False
    return arr_sort(arr, current + 1)

arr = list(map(int, input().split()))
if arr_sort(arr):
    print("Yes")
else:
    print("No")
