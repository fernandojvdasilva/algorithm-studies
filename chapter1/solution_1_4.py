'''
Created on 30 de set de 2017

@author: fernando
'''

''' Write a method to decide if two strings are anagrams or not. '''

def are_anagrams(str1, str2):
    chars_hash = {}
    
    result = True
    
    for i in range(len(str1)):
        if str1[i] in chars_hash.keys():
            chars_hash[str1[i]] += 1
        else:
            chars_hash[str1[i]] = 1 
        
    for i in range(len(str2)):
        if not str2[i] in chars_hash.keys():
            result = False
            break
        else:
            chars_hash[str2[i]] -= 1
    
    if result:
        for k in chars_hash.keys():
            if chars_hash[k] != 0:
                result = False
                break
                
    return result
            