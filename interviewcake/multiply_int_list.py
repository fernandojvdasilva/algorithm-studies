'''
Created on 5 de out de 2017

@author: fernando
'''

'''
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products. 
For example, given: 
 [1, 7, 3, 4]
 
your function would return: 
 [84, 12, 28, 21]
by calculating: 
 [7 * (3 * 4),  1 * (3 * 4),  (1 * 7) * 4,  (1 * 7) * 3]

 [1, 7, 3, 4, 5, 8]
 [ 7 * (3 * (4 * (5 * 8))), 
   1 * (3 * (4 * (5 * 8))), 
   1 * (7 * (4 * (5 * 8))), 
   (((1 * 7) * 3) * 5) * 8,    
   (((1 * 7) * 3) * 4) * 8,    
   (((1 * 7) * 3) * 4) * 5,   


Do not use division in your solution. 

'''


prev_results = {}

def get_products(integers, start, end):
    key = '%d-%d' % (start, end)

    if key in prev_results.keys():
        return prev_results[key]    

    result = 1

    if end-start > 1:
        result = integers[start] * get_products(integers, start+1, end)        
    else:
        result = integers[start]

    prev_results[key] = result
    return result


def get_products_of_all_ints_except_at_index(integers):
    result = []
    for i in range(len(integers)):
        a = 1
        b = 1
        if i < len(integers) - 1:
            a = get_products(integers, i+1, len(integers))
        if i > 0:
            b = get_products(integers, 0, i)

        result.append(a * b)

    return result

