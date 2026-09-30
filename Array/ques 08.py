# Move all zeros to the end

from array import *
val = array('i',[1,0,62,3,0,0,45,5,0,7])
result = []

for num in val:
    if num != 0:    
        result.append(num)
print(result)


zeros = len(val) - len(result)
for i in range(zeros):
    result.append(0)
print(zeros)
print(result)