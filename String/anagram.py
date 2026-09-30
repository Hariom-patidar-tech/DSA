def is_anagram(str1,str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

str1 = "hello"
str2 = "ohelo"

if is_anagram(str1,str2):
    print("anagram")
else:
    print("not anagram")