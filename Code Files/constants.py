cut_off = 'CUTOFF'

failure = 'FAILURE'

puzzle_0 = [[3,1,2],
            [7,'*',5],
            [4,6,8]]

puzzle_1 = [[7,2,4],
            [5,'*',6],
            [8,3,1]]

puzzle_2 = [[6,7,3],
            [1,5,2],
            [4,'*',8]]

puzzle_3 = [['*',8,6],
	        [4,1,3],
	        [7,2,5]]

puzzle_4 =	[[7,3,4],
		     [2,5,1],
		     [6,8,'*']]

puzzle_5 =	[[1,3,8],
		     [4,7,5],
             [6,'*',2]]

puzzle_6 = [[8,7,6],
            [5,4,3],
            [2,1,'*']]

puzzle_15_1 = [[13,10,11,6],
               [5,7,4,8],
               [1,12,14,9],
               [3,15,2,'*']]

puzzle_15_2 = [[13,10,11,6],
               [5,7,4,8],
               [2,12,14,9],
               [3,15,1,'*']]

goalBoard_15Puzzle = [['*',1,2,3],
                      [4,5,6,7],
                      [8,9,10,11],
                      [12,13,14,15]]

goalBoard_8Puzzle = [['*',1,2],
             [3,4,5],
             [6,7,8]]


# current selected board for execution 
board = puzzle_0

# current selected goal board for execution 
goalBoard = goalBoard_8Puzzle