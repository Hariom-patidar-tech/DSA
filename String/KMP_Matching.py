def kmp(text,pattern):
    if pattern in text:
        print("find")
    else:
        print("not find")
        
text = "abcdefghij"
pattern = "ghi"

kmp(text,pattern)