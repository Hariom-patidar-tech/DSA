# Count even and odd numbers

from array import *
val = array('i',[1,2,3,4,5,6,7,8,6])
even = odd = 0
for i in val:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(even,odd)