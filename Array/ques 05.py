# Check if an array is sorted or not

from array import *
val = array('i',[1,2,3,45,5,7])
is_sort = True
for i in range(len(val)-1):
    if val[i] > val[i+1]:
        is_sort = False
        break
if is_sort:
    print("sort")
else:
    print("not")