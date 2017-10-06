'''
Created on 29 de set de 2017

@author: fernando
'''


'''
Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?
'''


def has_all_unique_characters(string):
    ''' If I can use data structures, the obvious answer is to use a set (aka. hashset)
    Otherwise I can order it and reach to O(n log n)
    '''
    result = True
    
    sortedString = mergeSort(string)
    for i in range(1, len(sortedString)):
        if sortedString[i] == sortedString[i-1]:
            result = False
            break
        
    return result
        


def mergeSort(list):
    if len(list) == 1:
        return list
    else:
        list1 = list[:int(len(list)/2)]
        list2 = list[int(len(list)/2):]
        return merge(mergeSort(list1), mergeSort(list2))

def merge(a, b):
    results = [0] * (len(a)+len(b))
    a_i = b_i = r_i = 0
    
    while a_i < len(a) and b_i < len(b):
        if a[a_i] < b[b_i]:
            results[r_i] = a[a_i]
            a_i += 1
        else:
            results[r_i] = b[b_i]
            b_i += 1
        r_i += 1
        
    while a_i < len(a):
        results[r_i] = a[a_i]
        r_i += 1
        a_i += 1
    
    while b_i < len(b):
        results[r_i] = b[b_i]
        r_i += 1
        b_i += 1
        
    return results