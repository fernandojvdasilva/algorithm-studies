'''
Let’s say we have a group of 

N friends represented by a list of dictionaries where each value is a friend name and their location on a three dimensional scale of (
�
,
�
,
�
x,y,z). The friends want to host a party but want the friend with the optimal location (least distance to travel as a group) to host it.

Write a function pick_host to return the friend that should host the party.

Example:

Input:

friends = [
    {'name': 'Bob', location: (5,2,10)},
    {'name': 'David', location: (2,3,5)},
    {'name': 'Mary', location: (19,3,4)},
    {'name': 'Skyler', location: (3,5,1)},
]

def optimal_host(friends) -> 'David'


friends = [
    {'name': 'Bob', location: (5,2,10)},
    {'name': 'David', location: (2,3,5)},
    {'name': 'Mary', location: (19,3,4)},
    {'name': 'Skyler', location: (3,5,1)},
]


(5, 2, 10) - (2, 3, 5) = (5-2, 2-3, 10-5) = (3,-1,5) = sqrt(3**2 + -1**2 + 5**2) = 


{'host': 'Bob', 'sum': ]}


def optimal_host(friends) -> 'David'


'''

calculated_distances = {}

from math import sqrt

def calc_distance(friendA, friendB):
    key = '%s+%s' % (friendA['name'], friendB['name']) \
    if friendA['name'] < friendB['name'] \
    else '%s+%s' % (friendB['name'], friendB['name'])

    if key in calculated_distances.keys():
        return calculated_distances[key]

    locA = friendA['location']
    locB = friendB['location']

    distVec = [locA[i]-locB[i] for i in range(3)]
    mag = sqrt(distVec[0] ** 2 + distVec[1] ** 2 + distVec[2] ** 2)

    calculated_distances[key] = mag

    return mag

def pick_host(friends):
    for f in friends:
        for f_ in friends:
            if f == f_:
                continue
            dist = calc_distance(f, f_)
            if not 'total_dist' in f.keys():
                f['total_dist'] = dist
            else:
                f['total_dist'] += dist

    min_dist = float('inf')
    res = None
    for f in friends:
        if f['total_dist'] < min_dist:
            min_dist = f['total_dist']
            res = f['name']

    return res