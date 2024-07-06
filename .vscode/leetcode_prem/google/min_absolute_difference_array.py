'''
Given an array of integers, write a function min_distance to calculate the minimum absolute distance between two elements then return all pairs having that absolute difference.

Note: Make sure to return the pairs in ascending order.

Example:

Input:

v = [3, 12, 126, 44, 52, 57, 144, 61, 68, 72, 122]
Output:

def min_distance(V) ->

min = 4

[[57, 61], [68, 72], [122, 126]]


v = [3, 12, 126, 44, 52, 57, 144, 61, 68, 72, 122]

sorted
v = [3, 12, 44, 52, 57, 61, 68, 72, 122, 126, 144]

d =     [9, 32, 12, 5, 4, 7, 4, 50, 4, 18]
min = 4



'''
from math import sqrt
def min_distance(test_input):
    v = sorted(test_input)

    d = []
    min_dist = float('inf')
    for i in range(1, len(v)):
        distance = sqrt((v[i] - v[i-1])**2)
        if distance < min_dist:
            min_dist = distance
        d.append(distance)

    min_elements = []
    for i in range(len(d)):
        if d[i] == min_dist:
            min_elements.append([v[i], v[i+1]])


    return min_dist, min_elements