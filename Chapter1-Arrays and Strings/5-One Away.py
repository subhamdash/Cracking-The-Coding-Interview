# -*- coding: utf-8 -*-
"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, pIe -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false
"""

def one_away(s1,s2):
    
    m = len(s1) 
    n = len(s2) 
    if abs(m - n) > 1: 
        return False 
    
    count = 0    
    i = 0
    j = 0
    while i < m and j < n: 
        # If current characters dont match 
        if s1[i] != s2[j]: 
            if count == 1: 
                return False 
  

            if m > n: 
                i+=1
            elif m < n: 
                j+=1
            else:    
                i+=1
                j+=1
  
           
            count+=1
  
        else:    
            i+=1
            j+=1
  
    # if last character is extra in any string 
    if i < m or j < n: 
        count+=1
    if count==1:
        return True
    return False

s1='pates'
s2='pale'
print(one_away(s1,s2))