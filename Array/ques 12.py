
# Second Largest

def second_largest(arr):
    max = 0
    second = 0
    for i in arr:
        if i > max:
            second = max
            max = i
        else:
            if i< max and i > second:
                second = i
    return second

arr = [1,2,33,884,5]
obj = second_largest(arr)
print(obj)