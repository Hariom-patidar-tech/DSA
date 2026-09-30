# Find the frequency of each element

from array import *
val = array('i',[1,2,2,3,4,4,4,5,6,7,7,8])
freq = {}
for i in val:
    if i in freq:
        freq[i] +=  1
    else:
        freq[i] = 1
print(freq)