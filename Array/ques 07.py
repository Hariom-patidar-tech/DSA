# Remove duplicates from a sorted array
from array import *
val = array('i',[1,2,2,3,4,4,4,5,6,7,7,8])
vall = []
for i in val:
    if i not in vall:
        vall.append(i)
print(vall) 