'''
Created on 6 de out de 2017

@author: fernando
'''


'''
Given a list of integers, find the highest product you can get from three of the integers. 
The input list_of_ints will always have at least three integers. 
[-10, -10, 1, 3, 2]
[1, 3, -10, 2, -10]

Result = 300

'''

def find_highest_product(list_of_ints):
    neg_1 = neg_2 = 1
    pos_1 = pos_2 = pos_3 = -float('inf')
    for i in range(len(list_of_ints)):
        if list_of_ints[i] < 0:
            if list_of_ints[i] < neg_1:
                neg_2 = neg_1
                neg_1 = list_of_ints[i]
            elif list_of_ints[i] < neg_2:
                neg_2 = list_of_ints[i]

        if list_of_ints[i] > pos_1:
            pos_3 = pos_2
            pos_2 = pos_1
            pos_1 = list_of_ints[i]
        elif list_of_ints[i] > pos_2:
            pos_3 = pos_2
            pos_2 = list_of_ints[i]
        elif list_of_ints[i] > pos_3:
            pos_3 = list_of_ints[i]

    if (neg_1 * neg_2 * pos_1) > (pos_1 * pos_2 * pos_3):
        return (neg_1 * neg_2 * pos_1)
    else:
        return(pos_1 * pos_2 * pos_3)