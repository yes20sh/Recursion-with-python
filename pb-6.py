# Copy one string to another using recursion.

def copy_str(text, current = 0, des = ""):
    if current == len(text):
        return des
    des += text[current]
    return copy_str(text, current + 1, des)
  
text = input()
print(f"The new string : {copy_str(text)}")