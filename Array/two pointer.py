# Two Pointer Technique

def two_pointer(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

arr = [2, 7, 11, 15]
target = 17
result = two_pointer (arr, target)
print(result)


