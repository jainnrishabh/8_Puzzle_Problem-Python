# Reference : Wikipedia to understand the concept of 15 puzzle solvablility 
# Reference : https://chat.openai.com/ -> to understand the concept of inversion in puzzle 

import constants

puzzles = [ constants.puzzle_0 , constants.puzzle_1, constants.puzzle_2, constants.puzzle_3, constants.puzzle_4, constants.puzzle_5, constants.puzzle_6, constants.puzzle_15_1 , constants.puzzle_15_2]

def get_inversion_count(puzzle):
    count = 0 
    x_pos = -1
    linear = []
    N = len(puzzle)
    for i in range(N):
        for itm in puzzle[i]:
            linear.append(itm)
            if itm == None:
                x_pos = i
    for i in range(N * N - 1):
        for j in range(i + 1, N * N):
              if linear[i] != '*' and linear[j]!= '*' and linear[i] > linear[j]:
                  count += 1
    return count, x_pos

def is_solvable(puzzle):
    inversionCount, blankPos = get_inversion_count(puzzle)
    if len(puzzle) % 2:
        return not bool(inversionCount % 2)
    else:
        if blankPos % 2 == 0:
            return not bool(inversionCount % 2)
        else:
            return bool(inversionCount % 2)
    
for puzzle in puzzles:
    print(puzzle , 'Solvable') if is_solvable(puzzle) else print(puzzle, 'Not Solvable')