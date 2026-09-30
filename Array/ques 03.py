# Find the sum and average of elements

from array import *
val = array('i',[1,2,3,4,5,6,7,8])
sum = 0
for i in val:
    sum += i
    ave = sum / len(val)
    
print(sum)
print(ave)



arr = [1,2,3,4,5,6,7,8]

total = 0
for num in arr:
    total += num

avg = total / len(arr)

print("Sum:", total, "Average:", avg)