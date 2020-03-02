# -*- coding: utf-8 -*-
"""
1.6 String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def string_compressor(word):
    compressed_word = ""
    count_letter = ""
    count = 0
    
    for letter in word:
        if letter == count_letter:
            count += 1
        else:
            if count > 0:
                compressed_word += count_letter + str(count)
            count_letter = letter
            count = 1
    compressed_word += count_letter + str(count)
    
    if len(compressed_word) < len(word):
        return compressed_word
    else:
        return word

print(string_compressor('aabcccccaaa'))


