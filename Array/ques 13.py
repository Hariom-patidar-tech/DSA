#  Two Sum (Pair)

def sum(arr, target):
    for i in  range(len(arr)):
        for j in range(i+1,(len(arr))):
            if arr[i] + arr[j] == target:
                return [i,j]
    
arr = [2,5,5,11]
target = 10
obj = sum(arr,target)
print(obj)