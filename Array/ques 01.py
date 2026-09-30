# Find the maximum and minimum element in an array

from array import *
val = array('i',[11,22,19,14,55,16])

max_val = min_val = val[0]

for num in val:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max:", max_val, "Min:", min_val)