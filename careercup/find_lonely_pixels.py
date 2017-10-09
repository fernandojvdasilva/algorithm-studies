'''
Created on 9 de out de 2017

@author: fernando
'''

'''
Lonely Pixel 
Given an N x M image with black pixels and white pixels, if a pixel is the only one in its color throughout its entire row and column, then it is a lonely pixel. Find the number of lonely pixels in black from the image. (O(NM))

0 → black
1 → white
[ [0, 1, 1, 0, 0],
   [1, 1, 1, 1, 1],
   [0, 1, 0, 0, 1]
   [1, 0, 1, 1, 1] ]

result = 1

test # 2:
[ [0, 1, 1, 0, 0],
   [1, 1, 0, 1, 1],
   [0, 1, 0, 0, 1]
   [1, 0, 1, 1, 1] ]

'''

def find_lonely_pixels(image, n, m):
    count_rows = [0] * n
    count_cols = [0] * m
    for i in range(n):
        for j in range(m):
            if image[i][j] == 0:
                count_rows[i] += 1
                count_cols[j] += 1
    result = 0
    for i in range(len(count_rows)):
        if count_rows[i] == 1:
            for j in range(m):
                if image[i][j] == 0 and count_cols[j] == 1:
                    result += 1        
    return result