def reverse_string(s):
    stack = []
    
    for ch in s:
        stack.append(ch)
        
    reverse_string = ""
    
    while stack:
        reverse_string += stack.pop()
        
    return reverse_string


s = input("Enter the string  -> ")
print("reverse_string  ->",reverse_string(s))