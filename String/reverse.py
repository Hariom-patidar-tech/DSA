s  = "hariom"
rev = ""
for i in s:
    rev = i + rev
print(rev)




# Two pointers

def reverse(s):
    s = list(s)
    left = 0
    right = len(s)-1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
        
    return"".join(s)

s = "pointers"
print(reverse(s))