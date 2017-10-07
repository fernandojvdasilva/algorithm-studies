'''
Created on 7 de out de 2017

@author: fernando
'''

'''

Given 2 words, return true if second word has a substring that is also an anagram of word 1. 
LGE , GOOGLE- True 
GEO, GOOGLE – False

'''

from copy import copy
def build_anagram_map(str1):
    char_count = {}
    for i in range(len(str1)):
        if str1[i] in char_count.keys():
            char_count[str1[i]] += 1
        else:
            char_count[str1[i]] = 1
    return char_count

def check_anagram(anagram_map, str2):
    char_count = copy(anagram_map)
    anagrams = True
    for i in range(len(str2)):
        if str2[i] in char_count.keys():
            char_count[str2[i]] -= 1
        else:
            anagrams = False
            break
    if anagrams:
        for k in char_count.keys():
            if char_count[k] > 0:
                anagrams = False
                break
    return anagrams
        

def check_anagram_substring(str1, str2):
    m = len(str1)
    anagram_map =  build_anagram_map(str1)
    result = False
    for i in range(0, len(str2), m):
        result =  result or check_anagram(anagram_map, str2[i:i+m])

    return result