


"""2-Check Permutation: Given two strings, write a method to decide if one is permutation of other"""

def check_permutation(s,z):
    store=[0]*26
    if len(s)!=len(z):
        return False
    for i in s:
        store[ord(i)-ord('a')]+=1
    for i in z:
        store[ord(i)-ord('a')]-=1
        if store[ord(i)-ord('a')]<0:
            return False
 
    return True
    

s='abbbacbaaccad'
z='cccabbbaaabdb'
print(check_permutation(s,z))