"""1.IS Unique:Implement an algorithm to detrmine if a string has all unique characters."""

def is_unique(s):
    d=s.lower()
    x=[0]*26
    for i in d:
        if x[ord(i)-ord('a')]==0:
            x[ord(i)-ord('a')]=1
        else:
            return False
    return True

d='thisago'
print(is_unique(d))
            