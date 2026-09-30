# Rotate an array by k positions
from array import *
val = array('i',[1,2,3,4,5,6,7,8,6])
k = 2
n = len(val)
k = k % n

rotate = val[-k:] + val[:-k]
print(rotate)