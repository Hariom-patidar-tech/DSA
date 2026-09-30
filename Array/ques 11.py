#  Find largest

def find_max(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max
        
arr = [2,33,44,11,445,666,33]
obj = find_max(arr)
print(obj)