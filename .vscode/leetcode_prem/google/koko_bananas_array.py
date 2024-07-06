'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
'''
class Solution:

    '''
    Input: piles = [3,6,7,11], h = 8
    Output: 4


    piles = [3, 
             6, 
             7,
             11]

    if h (the number of visits) is equals len(piles), get max piles
    if h > len(piles), 

    
    piles = [3, (1)
             6, (2)
             7, (3)
             11] (4)

    num_visits = len(piles) - h = 4

    '''

    import copy

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)

        
        
        if h == len(piles):
            return piles[-1]

        elif h > len(piles):
            all_bananas = 0
            for i in range(len(piles)):
                all_bananas += piles[i]

            piles_copy = copy.deepcopy(piles)
            k = piles[0]
            while k < piles[-1]+1:

                piles = piles_copy
                i = len(piles)-1
                while h > 0:
                    if i < 0:
                        i = len(piles)-1
                    if piles[i] == 0:
                        i -= 1
                        continue
                    
                    if piles[i] - k > 0:
                        piles[i] -= k
                        all_bananas -= k
                    else:
                        all_bananas -= piles[i]
                        piles[i] = 0
                        
                    h -= 1
                    i -= 1

                if all_bananas == 0:
                    break
                
                k += 1

        else:
            print("Can't eat all the bananas")
        
        return k