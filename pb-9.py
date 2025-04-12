# Find the largest element of an array using recursion.

def largest_element(arr, index = 0):
    if index == len(arr) - 1:
        return arr[index]
    max_in_rest = largest_element( arr, index + 1)
    return arr[index] if arr[index] > max_in_rest else max_in_rest
   
arr = list(map(int, input().split()))
print(largest_element(arr))