def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n -i -1):
            if  arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                
    return arr

arr = [11,23,10,4,78]
obj = bubble(arr)
print(obj)
                
        
arr = [1,3,5,2,12,23,34,5]

for i in range(len(arr)):
    for j in range(i, len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1], arr[j]
            
print(arr)