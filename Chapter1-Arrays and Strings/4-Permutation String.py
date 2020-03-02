# -*- coding: utf-8 -*-
"""
1.4 -Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
"""

def is_pall(s):
    
    l=[]
    for i in s:
        if i ==' ':
            continue
        if i in l:
            l.remove(i)
        else:
            l.append(i)
    if (len(s)%2==0 and len(l)==0) or (len(s)%2==1 and len(l)==1):
        return True
    return False
s='tacocat'
print(is_pall(s))


