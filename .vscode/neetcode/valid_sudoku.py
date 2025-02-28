'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_masks = [0] * 9
        col_masks = [0] * 9
        box_masks = []
        for i in range(3):
            box_masks.append([0, 0, 0])

        res = True

        #print("box_masks")
        #print(box_masks)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue

                curr_mask = 1 << int(board[i][j])


                box_i = 0 if i < 3 else 1 if i < 6 else 2
                box_j = 0 if j < 3 else 1 if j < 6 else 2

                if curr_mask & row_masks[i] != 0 or \
                curr_mask & col_masks[j] != 0 or \
                curr_mask & box_masks[box_i][box_j] != 0:

                    #print("box_masks")
                    #print(box_masks)
                    #print("--")
                    #print("curr_mask = %d" % curr_mask)
                    #print("row_masks[%d] = %d" % (i, row_masks[i]))
                    #print("col_masks[%d] = %d" % (j, col_masks[j]))
                    #print("box_masks[%d][%d] = %d" % (box_i, box_j, box_masks[box_i][box_j]))

                    #print("curr_mask & row_masks[%d] = %s" % (i, str(curr_mask & row_masks[i])))
                    #print("curr_mask & col_masks[%d] = %s" % (j, str(curr_mask & col_masks[j])))
                    #print("curr_mask & box_masks[%d][%d] = %s" % (box_i, box_j, str(curr_mask & box_masks[box_i][box_j])))

                    res = False
                    break
                else:
                    row_masks[i] |= curr_mask
                    col_masks[j] |= curr_mask
                    box_masks[box_i][box_j] |= curr_mask
                
            
            if not res:
                break

        return res
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_masks = [0] * 9
        col_masks = [0] * 9
        box_masks = []
        for i in range(3):
            box_masks.append([0, 0, 0])

        res = True

        #print("box_masks")
        #print(box_masks)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue

                curr_mask = 1 << int(board[i][j])


                box_i = 0 if i < 3 else 1 if i < 6 else 2
                box_j = 0 if j < 3 else 1 if j < 6 else 2

                if curr_mask & row_masks[i] != 0 or \
                curr_mask & col_masks[j] != 0 or \
                curr_mask & box_masks[box_i][box_j] != 0:

                    #print("box_masks")
                    #print(box_masks)
                    #print("--")
                    #print("curr_mask = %d" % curr_mask)
                    #print("row_masks[%d] = %d" % (i, row_masks[i]))
                    #print("col_masks[%d] = %d" % (j, col_masks[j]))
                    #print("box_masks[%d][%d] = %d" % (box_i, box_j, box_masks[box_i][box_j]))

                    #print("curr_mask & row_masks[%d] = %s" % (i, str(curr_mask & row_masks[i])))
                    #print("curr_mask & col_masks[%d] = %s" % (j, str(curr_mask & col_masks[j])))
                    #print("curr_mask & box_masks[%d][%d] = %s" % (box_i, box_j, str(curr_mask & box_masks[box_i][box_j])))

                    res = False
                    break
                else:
                    row_masks[i] |= curr_mask
                    col_masks[j] |= curr_mask
                    box_masks[box_i][box_j] |= curr_mask
                
            
            if not res:
                break

        return res