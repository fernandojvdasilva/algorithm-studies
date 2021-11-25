'''
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and
 columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction,
then one square in an orthogonal direction.




Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go
off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability
that the knight remains on the board after it has stopped moving.

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Note:

    N will be between 1 and 25.
    K will be between 0 and 100.
    The knight always initially starts on the board.


'''

class Solution:

    ''' SOLUTION: Let's think about a recursive solution.
        At each point, we have 8 possible moves. I'm thinking about a recursive function that calculates
        how many moves are valid (aka. inside the board) and call it recursively for each valid call.
    '''

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        ROW_IND = 0
        COL_IND = 1

        # We could think of a code comprehension to do that, but let it go...
        test_pos = [(r+2, c-1), (r+2, c+1), (r-2, c-1), (r-2, c+1)]
        test_pos += [(r-1, c+2), (r+1, c+2), (r-1, c-2), (r+1, c-2)]

        prob = 0.0
        num_valid = 0

        for pos in test_pos:

            if not (pos[ROW_IND] < 0 or pos[ROW_IND] > N or \
                pos[COL_IND] < 0 or pos[COL_IND] > N):

                num_valid += 1
                # If we can move
                if K > 1:
                    prob += self.knightProbability(N, K-1, pos[ROW_IND], pos[COL_IND])

        if K == 1:
            prob = float(num_valid)

        return prob / 8.0


