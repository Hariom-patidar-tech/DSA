# Find the second largest element

from array import *
val = array('i',[1,62,3,45,5,7])
n = len(val)
largest = val[n-1]
second = 0
for num in val:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)