arr = [10,20,30,40,5,10,50]
current_sum = arr[0]
max_sum = arr[0]
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        current_sum += arr[i]
    else:
        current_sum = arr[i]
        
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)