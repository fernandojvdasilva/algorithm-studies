'''
Created on 3 de out de 2017

@author: fernando
'''
from copy import deepcopy



def solve_sudoku(initial_game):
        game = deepcopy(initial_game)
        
        initialize(game)
        
        last_i = []
        last_j = []
        
        i = j = 0
        
        n_initial = 1

        while j < len(game[0]):
            if game[i][j] == initial_game[i][j]: # Posiciona o primeiro número "novo"
                if i < len(game):
                    i += 1
                else:
                    i = 0
                    j += 1
                continue
            found_number = False
            n = n_initial
            
            while n < 10 and not found_number:
                n_valid = True
                i_ = j_ = 0
                while i_ < len(game):
                    if n == game[i_][j]:
                        n_valid = False
                        break
                    i_ += 1
                
                if not n_valid:
                    n += 1
                    continue
                
                while j_ < len(game[i]):
                    if n == game[i][j_]:
                        n_valid = False
                        break
                    j_ += 1
                
                if not n_valid:
                    n += 1
                    continue
                    
                box_limit_i = 0
                box_limit_j = 0
                
                if i < 3:
                    i_ = 0
                    box_limit_i = 3
                elif i < 6:
                    i_ = 3
                    box_limit_i = 6
                elif i < 9:
                    i_ = 6
                    box_limit_i = 9
                    
                while i_ < box_limit_i and n_valid:
                    if j < 3:
                        j_ = 0
                        box_limit_j = 3
                    elif j < 6:
                        j_ = 3
                        box_limit_j = 6
                    elif j < 9:
                        j_ = 6
                        box_limit_j = 9
                                        
                    while j_ < box_limit_j:
                        if n == game[i_][j_]:
                            n_valid = False
                            break           
                        j_ += 1
                    
                    i_ += 1
                    
                if not n_valid:
                    n += 1
                    continue
                    
                if n < 10:
                    found_number = True
            
            if found_number:
                game[i][j] = n
                last_i.append(i)
                last_j.append(j)
                if i < len(game)-1:
                    i += 1
                else:
                    i = 0
                    j += 1
                n_initial = 1
            else:
                i = last_i.pop()
                j = last_j.pop()
                n_initial = game[i][j] + 1
                game[i][j] = None                
                
                
        return game

def initialize(game):
    i = j = 0
    while i < len(game) and j < len(game[i]):
        if game[i][j] == 0:
            game[i][j] = None
            
        j += 1
        if j == len(game[i]):
            i += 1
            j = 0